.. index:: Geometry Nodes; Interpolate Curves
.. _bpy.types.GeometryNodeInterpolateCurves:

***********************
Interpolate Curves Node
***********************

.. figure:: /images/node-types_GeometryNodeInterpolateCurves.png
   :align: right
   :alt: Interpolate Curves node.

Generate new curves on points by interpolating between existing curves.


Inputs
======

Guide Curves
   Base curves that new curves are interpolated between.
Guide Up
   Optional up vector that is typically a surface normal.
Guide Group ID
   Splits guides into separate groups. New curves interpolate existing curves from a single group.
Points
   First control point positions for new interpolated curves.
Points Up
   Optional up vector that is typically a surface normal.
Point Group ID
   The curve group to interpolate in.
Max Neighbor
   Maximum amount of close guide curves that are taken into account for interpolation.


Properties
==========

This node has no properties.


Outputs
=======

Curves
   The guide curves with interpolated curves.
Closest Index
   Index of the closest guide curve for each generated curve.
Closest Weight
   Weight of the closest guide curve for each generated curve.
