.. index:: Compositor Nodes; Render Layers
.. _bpy.types.CompositorNodeRLayers:

******************
Render Layers Node
******************

.. figure:: /images/node-types_CompositorNodeRLayers.webp
   :align: right
   :alt: Render Layers Node.

The *Render Layers* node renders a :doc:`View Layer </render/layers/introduction>`
from a scene and outputs its image and any enabled
:doc:`render passes </render/layers/passes>` to the compositor.
This allows render results to be combined, processed, or composited with other
images and render layers.


Inputs
======

This node has no input sockets.


Properties
==========

Scene
   The scene for which to render a view layer.

View Layer
   The view layer to render. The button next to the dropdown re-renders it immediately.

.. hint::

   To use the composited output of another scene instead of its raw render
   passes, first render that scene to a multilayer image format such as
   :doc:`OpenEXR </files/media/image_formats>`. The resulting image can then be
   loaded using the :doc:`Image </compositing/types/input/image>` node.


Outputs
=======

Image
   The combined rendered image.

Alpha
   The alpha channel of the rendered image.

Additional outputs corresponding to the render passes enabled for the selected view layer.

.. note::

   The :ref:`Viewport Compositor <bpy.types.View3DShading.use_compositor>`
   only provides render pass outputs when using EEVEE. With other render
   engines, these outputs are empty.
