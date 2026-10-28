.. index:: Compositor Nodes; Viewer
.. _bpy.types.CompositorNodeViewer:

***********
Viewer Node
***********

.. figure:: /images/node-types_CompositorNodeViewer.webp
   :align: right
   :alt: Viewer Node.

The *Viewer* node previews image data or value maps at any point within a compositor node tree.
It allows intermediate results to be inspected without affecting the final composited image.

A Viewer node can be quickly connected to another node by pressing :kbd:`Shift-Ctrl-LMB` on that node.
To switch between multiple Viewer nodes, select one with :kbd:`LMB`.
The active Viewer node is indicated by the :bl-icon:`restrict_view_off` icon in its header.

When using :doc:`Scene Effects </compositing/scene_effects>`, only Viewer nodes
belonging to the active effect can control the preview.
If the active effect has no active Viewer node, Blender displays the final
output of the effects stack instead.

.. note::

   Viewer nodes are optional. When no active Viewer node is available,
   Blender uses the output of the node tree for interactive previews.
   This allows the final result to be displayed without adding a Viewer node.


Inputs
======

Image
   Outputs the result of this input directly to the viewer result.
   If this socket is left unconnected, the output will be a black image.


Outputs
=======

This node has no output sockets.


Usage
=====

Compositor Backdrop
-------------------

When a Viewer node is active and :ref:`bpy.types.SpaceNodeEditor.show_backdrop` is enabled,
its image is displayed behind the node tree as a backdrop. This allows compositing operations
to be evaluated directly while editing the node graph.

When the active Viewer node is selected, an interactive gizmo is displayed in the backdrop
if :ref:`bpy.types.SpaceNodeEditor.show_gizmo_active_node` is enabled. The gizmo can be used to:

- Move the backdrop image.
- Scale the backdrop image.

These adjustments only affect how the image is displayed in the Node Editor and do not
modify the image itself or the compositor output.


.. _bpy.ops.node.viewer_shortcut_set:
.. _bpy.ops.node.viewer_shortcut_get:

Keyboard Shortcuts
------------------

Viewer nodes provide a quick way to toggle between different viewer nodes while compositing using keyboard shortcuts,
improving workflow efficiency when comparing outputs.

- **Assign Shortcut** (:kbd:`Ctrl-1`, :kbd:`Ctrl-2`, etc.):
  Select a node and press a shortcut to assign it. If no Viewer node is attached, one is created and activated.
  The number will be shown in the upper right part of the node to identify which shortcut is assigned.
- **Activate Node** (:kbd:`1`, :kbd:`2`, etc.):
  Press the assigned number key to activate the node's Viewer output.

.. note:: Only number keys (`1-9`) are supported.


Using the Image Editor
----------------------

The Viewer result can be displayed in the Image Editor by selecting
*Viewer Node* from the *Image* data-block menu in its header.

The Image Editor displays the result of the active Viewer node.
When no active Viewer node is available, the final compositor output is displayed instead.

To save the displayed image, use :menuselection:`Image --> Save As...`
or :kbd:`Alt-S`.

The Image Editor also provides controls for displaying the color channels,
alpha channel, or depth information.
Clicking and holding :kbd:`LMB` over the image allows pixel values to be inspected.

.. seealso::

   For overlays specific to the Viewer node, such as text information and render guides,
   see :ref:`Guides Overlays <editors-image-overlays-guides>`.
