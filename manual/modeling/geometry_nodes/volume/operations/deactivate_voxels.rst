.. index:: Geometry Nodes; Deactivate Voxels
.. _bpy.types.GeometryNodeGridDeactivateVoxels:

**********************
Deactivate Voxels Node
**********************

.. figure:: /images/node-types_GeometryNodeGridDeactivateVoxels.webp
   :align: right
   :alt: Deactivate Voxels node.

The *Deactivate Voxels* node deactivates any active voxels or tiles of a grid where the *Selection*
field is *true*. The *Selection* field is evaluated at every voxel and tile position of the input
grid.

The values of the output grid are unchanged, only the active state is changed.


Inputs
======

Grid
   A grid whose voxels will be deactivated based on the *Selection* field.

Selection
   Boolean field defining which voxels to deactivate.


Outputs
=======

Grid
   The resulting grid after voxels and tiles have been deactivated.
