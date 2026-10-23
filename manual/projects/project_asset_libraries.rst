.. _projects-asset_libraries:

***********************
Project Asset Libraries
***********************

A Blender Project can have its own :doc:`Asset Libraries
</files/asset_libraries/introduction>` that are automatically loaded only when
you're in that project. This lets you have asset libraries specific to your
project without polluting your list of general asset libraries when outside of
that project.

To manage the asset libraries of your project, go to :menuselection:`Project -->
Settings... --> Asset Libraries`

.. figure:: /images/projects_project_settings_asset_libraries.png

The management of your project asset libraries here is generally the same as
:ref:`normal asset libraries <bpy.types.UserAssetLibrary>`.

.. note::

   We recommend keeping your project asset libraries somewhere under your
   project root.

   If you do, and you select the library path via the file browser, the path
   will automatically use the ``{project_root}`` variable expression to make
   the path project-relative. This ensures that your project asset libraries
   travel with your project, and are available no matter where on disk you put
   your project.
