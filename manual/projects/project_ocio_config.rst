.. _projects-ocio_config:

**************************
Project OCIO Configuration
**************************

A Blender Project can have its own custom :ref:`OpenColorIO configuration <ocio-config>`.
This configuration will be automatically loaded and used for blend files in the project.

This approach helps ensure consistent color management throughout a project.

Selecting a Custom Configuration
================================

Go to :menuselection:`Project --> Settings... --> General` and expand the *Color Management* panel.

.. figure:: /images/projects_project_settings_ocio.png

In the *OpenColorIO Configuration* dropdown you can select from a set of
built-in configurations that come with Blender, or you can select the *Path*
option.

The *Path* option lets you browse to and select a custom OpenColorIO
configuration on disk:

.. figure:: /images/projects_project_settings_ocio_path.png

.. note::

   When using the *Path* option, we recommend keeping your on-disk OpenColorIO
   configuration somewhere under your project root.

   If you do so, and you select the configuration path via the file browser,
   the path will automatically use the ``{project_root}`` variable expression
   to make the path project-relative. This ensures that your OpenColorIO
   configuration travels with your project, and works no matter where on disk
   you put your project.
