
.. index:: Compositor Nodes; Bloom

**********
Bloom Node
**********

.. figure:: /images/node-types_CompositorNodeBloom.webp
   :align: right
   :alt: Glare Node.

.. --- modifier-intro-start ---

*Bloom* adds a soft glow around bright areas of an image,
simulating the scattering of light in camera lenses and the human eye.
This is particularly useful for enhancing emissive materials, lights,
and other bright highlights.

The asset uses a :doc:`Glare Node </compositing/types/filter/glare>`
with its glare type set to *Bloom*.
The glare type is exposed, allowing other effects such as
*Fog Glow* and *Streaks* to be used instead.

.. --- modifier-intro-end ---

Inputs
======

.. --- modifier-options-start ---

.. include:: /compositing/types/filter/glare.rst
   :start-after: .. glare-inputs-start
   :end-before: .. glare-inputs-end

.. --- modifier-options-end ---


Outputs
=======

.. include:: /compositing/types/filter/glare.rst
   :start-after: .. glare-outputs-start
   :end-before: .. glare-outputs-end
