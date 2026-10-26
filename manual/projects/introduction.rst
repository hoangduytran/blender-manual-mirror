************
Introduction
************

A Blender Project is a directory that contains a ``.blender_project`` subdirectory with a valid project
configuration in it. The directory that contains the ``.blender_project`` is called the "project root",
and all files under the project root are considered part of that Blender Project.

Opening a blend file that's inside a Blender Project will automatically load the project as well,
which gives you access to various project features.

.. note::

   Blender's Project feature is completely optional to use. Blender's single-file workflows will always keep working.
   If you already have your own approach for managing projects, feel free to keep doing that.

   However, Blender's Project system does provide a lot of niceties, so we recommend giving it try.


Creating Projects
=================

To create a new Blender Project, select :menuselection:`File --> Project --> New...`:

.. figure:: /images/projects_new_menu.png

A file browser will pop up. Navigate to the desired root directory of your project,
and click the *New Project* button.


Opening Projects
================

Typically you don't need to explicitly open projects: they are loaded
automatically when you open any blend file under their root directory.

However, sometimes you may want to open a project explicitly. To do this, you
can either select :menuselection:`File --> Project --> Open...` and navigate to
the desired project's root directory with the file browser, or you can select a
project from the list of recently opened projects (also under
:menuselection:`File --> Project`).

.. figure:: /images/projects_open_menu.png

Project Settings
================

When there's an open project, an additional :menuselection:`Project` menu will
appear in the top menu bar:

.. figure:: /images/projects_top_project_menu.png

Select :menuselection:`Project --> Settings...` to open the settings of the
current project:

.. figure:: /images/projects_project_settings.png

Here you can set the name of the project and, if desired, create a custom splash
screen image for it.

Additionally, you can set up a custom OCIO config, project asset libraries, etc.
See the feature-specific documentation links below for more details.

Features
========

When working within a Blender Project, you get access to the following project
features:

:ref:`Project Variables <projects-variables>`
   Custom key-value pairs that can be used inside :ref:`Path Templates
   <files-path_templates>`. This lets you define common filepaths, etc. in one
   place, to then be used by reference throughout your project's blend files.
:ref:`Project Asset Libraries <projects-asset_libraries>`
   :ref:`Asset libraries <asset_libraries-introduction>` that are only
   loaded when you're working on files inside that project. This lets you have
   project-specific assets to use within the project, without polluting your
   asset libraries outside of the project.
:ref:`Project OCIO Config <projects-ocio_config>`
   Define a custom :ref:`OpenColorIO configuration <ocio-config>` for your
   project, that's automatically used when working on files inside the project.
   This helps ensure that color management is consistent within the project,
   even when working with a custom configuration.
