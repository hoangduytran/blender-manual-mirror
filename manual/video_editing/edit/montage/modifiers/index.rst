.. index:: Modifiers; Video Sequencer Modifiers
.. index:: Video Sequencer Modifiers
.. _bpy.types.StripModifier:

***************
Strip Modifiers
***************

.. reference::

   :Panel:     :menuselection:`Properties Editor --> Strip Modifiers`

.. figure:: /images/video-editing_sequencer_strip_modifiers_panel.webp
   :align: right
   :scale: 75%

Modifiers are used to make adjustments to the image, like contrast,
brightness, saturation, color balance and applying masks.

You can add these modifiers directly to a media strip,
or you can use them within an :doc:`Adjustment Layer </video_editing/edit/montage/strips/adjustment>`
strip, making them apply to several media strips in one go.


Common Options
==============

Each modifier provides several controls in its header:

:bl-icon:`restrict_view_on` / :bl-icon:`restrict_view_off` Viewport
   Toggles the modifier effect in the Preview region.
:bl-icon:`restrict_render_on` / :bl-icon:`restrict_render_off` Render
   Enables or disables the modifier during rendering and final output.
   This can be useful for comparing the strip with and without the modifier applied.

.. _bpy.ops.sequencer.strip_modifier_duplicate:

Extras
   Duplicate :kbd:`Shift-D`
      Creates a duplicate of the modifier just below current one in the stack.

   .. _bpy.ops.sequencer.strip_modifier_copy:

   Copy to Selected
      Copies the modifier from the :term:`Active` strip to all selected strips.

   .. _bpy.ops.sequencer.strip_modifier_move_to_index:

   Move to First/Last
      Moves the modifier to the first or last position in the modifier stack.

   .. _bpy.types.SequencerCompositorModifierData.show_group_selector:

   Show Node Group
      For :ref:`Compositor Modifiers <bpy.types.SequencerCompositorModifierData>`,
      shows or hides the node group selector.

:bl-icon:`x` Remove Strip Modifier
   Removes the modifier from the modifier stack.
:bl-icon:`grip` Move Strip Modifier
   Drag to reorder modifiers in the stack.

   Modifiers are evaluated from top to bottom, so changing their order affects the final result.


Types
=====

Currently, the following modifiers are supported:

Image Modifiers
---------------

.. toctree::
   :maxdepth: 1
   :class: toc-list

   brightness_contrast.rst
   color_balance.rst
   compositor.rst
   curves.rst
   hue_correct.rst
   mask.rst
   tone_map.rst
   white_balance.rst


Sound Modifiers
---------------

.. toctree::
   :maxdepth: 1
   :class: toc-list

   echo.rst
   pitch.rst
   sound_equalizer.rst
