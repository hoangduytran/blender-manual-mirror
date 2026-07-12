import argparse

import sys
import os
import re

from enum import Enum
from pathlib import Path
from urllib.parse import quote

import requests

from make_utils import check_output

from typing import (
    List,
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--git-command", default="git")
    return parser.parse_args()


# Host used when the manual repo's remotes can't be probed (e.g. the script is
# run outside a clone). Normally the host is derived from the manual's own
# "origin"/"upstream" remote, so forks and mirrors work without editing this.
default_server_host = "projects.blender.org"
repo_api_repo = "blender/blender-manual-translations"
repo_api_contents = "contents"
repo_api_ref = "main"

_server_host = None

# Named capture group used to pull the host out of a git remote URL.
REMOTE_HOST_GROUP = "host"


class RemoteHostPattern(Enum):
    """Regexes matching the two git remote URL forms, each capturing the host."""
    # scp-like SSH syntax: [user@]host:path (colon not followed by "//").
    SSH = re.compile(rf"^(?:[^@/]+@)?(?P<{REMOTE_HOST_GROUP}>[^/:]+):(?!//)")
    # scheme://[user@]host[:port]/path
    URL = re.compile(rf"^[a-zA-Z][\w+.-]*://(?:[^@/]+@)?(?P<{REMOTE_HOST_GROUP}>[^/:]+)")


def run_git(path: Path, commands: List, exit_on_error: bool = True) -> str:
    args = parse_arguments()

    return check_output([args.git_command, "-C", path] + commands, exit_on_error)


def get_manual_git_root() -> str:
    return check_output([args.git_command, "rev-parse", "--show-toplevel"])


def parse_remote_host(url: str) -> str:
    url = url.strip()
    for pattern in RemoteHostPattern:
        match = pattern.value.match(url)
        if match:
            return match.group(REMOTE_HOST_GROUP)
    return ""


def get_server_host() -> str:
    # Derive the host from the manual repo's own remotes, so this script follows
    # forks/mirrors without edits; fall back to the default if none is found.
    global _server_host
    if _server_host is not None:
        return _server_host

    manual_dir = get_manual_git_root()
    for remote in ("origin", "upstream"):
        host = parse_remote_host(run_git(manual_dir, ["remote", "get-url", remote], exit_on_error=False))
        if host:
            _server_host = host
            return _server_host

    _server_host = default_server_host
    return _server_host


def get_repo_url_git() -> str:
    return f"https://{get_server_host()}/{repo_api_repo}.git"


def locale_exists() -> bool:
    locale_dir = os.path.join(get_manual_git_root(), "locale")
    if os.path.exists(locale_dir):
        return True

    return False


def get_lang_code():
    print("Enter the language code for the language you would like to checkout:")
    return str(input())


def get_lang_api_url(lang: str) -> str:
    lang = quote(lang.strip().lower(), safe="")
    repo_api_url_base = f"https://{get_server_host()}/api/v1/repos/"
    return f"{repo_api_url_base}{repo_api_repo}/{repo_api_contents}/{lang}?ref={repo_api_ref}"


def check_lang_exists(lang: str) -> bool:
    url = get_lang_api_url(lang)

    try:
        url_status = requests.get(url, timeout=10).status_code
    except requests.RequestException as ex:
        print(f"Could not check language code {lang!r}: Exception:{ex}")
        return False

    if url_status == 404:
        print(f"Status: {url_status}. No translation files found for language code {lang!r}, at URL: {url}.")
        return False

    if url_status == 200:
        return True

    print(f"Unexpected response while checking language code {lang!r}: HTTP {url_status}, tried URL: {url}")
    return False


def partial_checkout(lang: str):
    manual_dir = get_manual_git_root()
    locale_dir = os.path.join(manual_dir, "locale")

    print(run_git(manual_dir, ["clone", "--filter=blob:none", "--no-checkout", get_repo_url_git(), locale_dir]))
    run_git(locale_dir, ["sparse-checkout", "set", "--cone"])
    run_git(locale_dir, ["sparse-checkout", "add", lang])
    print(run_git(locale_dir, ["checkout", "main"]))


if __name__ == "__main__":
    args = parse_arguments()

    if locale_exists():
        print("locale directory already exists quitting")
        sys.exit(1)

    lang = get_lang_code().strip().lower()

    if not check_lang_exists(lang):
        sys.exit(1)

    partial_checkout(lang)
