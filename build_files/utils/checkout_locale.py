import argparse

import sys
import os

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


repo_url_git = "https://projects.blender.org/blender/blender-manual-translations.git"
repo_api_url_base = "https://projects.blender.org/api/v1/repos/"
repo_api_repo = "blender/blender-manual-translations"
repo_api_contents = "contents"
repo_api_ref = "main"


def run_git(path: Path, commands: List, exit_on_error: bool = True) -> str:
    args = parse_arguments()

    return check_output([args.git_command, "-C", path] + commands, exit_on_error)


def get_manual_git_root() -> str:
    return check_output([args.git_command, "rev-parse", "--show-toplevel"])


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

    print(run_git(manual_dir, ["clone", "--filter=blob:none", "--no-checkout", repo_url_git, locale_dir]))
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
