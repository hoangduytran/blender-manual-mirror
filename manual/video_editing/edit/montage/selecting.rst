
****************
Selecting Strips
****************

The active sequence strip is displayed with a light outline.
The *entire* strip can be selected by clicking :kbd:`LMB` in the middle of the strip.


.. _bpy.ops.sequencer.select_all:

Select All
==========

.. reference::

   :Menu:      :menuselection:`Select --> All`
   :Shortcut:  :kbd:`A`

Selects all the strips in the timeline.


Select None
===========

.. reference::

   :Menu:      :menuselection:`Select --> None`
   :Shortcut:  :kbd:`Alt-A`

Deselects all the strips in the timeline.


Invert Selection
================

.. reference::

   :Menu:      :menuselection:`Select --> Invert`
   :Shortcut:  :kbd:`Ctrl-I`

Inverts the current selection.


.. _bpy.ops.sequencer.select_box:

Box Select
==========

.. reference::

   :Menu:      :menuselection:`Select --> Box Select`
   :Shortcut:  :kbd:`B`


See :ref:`Box Select <bpy.ops.*.select_box>`.


Box Select (Include Handles)
============================

.. reference::

   :Menu:      :menuselection:`Select --> Box Select (Include Handles)`
   :Shortcut:  :kbd:`Ctrl-B`

Works like :ref:`Box Select <bpy.ops.*.select_box>`, but also selects any strip handles inside the box.
If a strip has only one handle selected, dragging it will change the strip's length.
If both handles are selected, the complete strip moves instead.


.. _bpy.ops.sequencer.select_less:

Select Less
===========

.. reference::

   :Menu:      :menuselection:`Select --> Less`
   :Shortcut:  :kbd:`Ctrl-NumpadMinus`

Removes neighboring strips from the selection.


.. _bpy.ops.sequencer.select_more:

Select More
===========

.. reference::

   :Menu:      :menuselection:`Select --> More`
   :Shortcut:  :kbd:`Ctrl-NumpadPlus`

Adds neighboring strips to the selection.


.. _bpy.ops.sequencer.select_by_type:

Select All by Type
==================

.. reference::

   :Menu:      :menuselection:`Select --> Select All by Type`

Selects strips of a specified type.

Type
   The type of strip to select.

   :Scene: Selects all Scene strips.
   :Clip: Selects all Movie Clip strips.
   :Mask: Selects all Mask strips.
   :Movie: Selects all Movie strips.
   :Sound: Selects all Sound strips.
   :Image: Selects all Image strips.
   :Color: Selects all Color strips.
   :Text: Selects all Text strips.
   :Adjustment Layer: Selects all Adjustment Layer strips.
   :Compositor: Selects all Compositor strips.
   :Effect: Selects all effect strips.
   :Visual: Selects all strips that can produce an image in the preview, excluding Sound strips.

Extend
   Adds matching strips to the current selection.
   When disabled, the existing selection is cleared before selecting matching strips.

Same Channel
   Only selects matching strips on the same channel as the active strip.
   This option only applies when the operator is invoked from the timeline.


.. _bpy.ops.sequencer.select_grouped:

Select Grouped
==============

.. reference::

   :Menu:      :menuselection:`Select --> Select Grouped`
   :Shortcut:  :kbd:`Shift-G`

Selects strips that share a property or relationship with the active strip.

Type
   The property or relationship used to determine which strips are selected.

   :Type:
      Selects all strips of the same specific type as the active strip.
   :Data:
      Selects strips referencing the same source data as the active strip,
      with matching file directory, scene, clip, or mask.
   :Strips Under Effect:
      Selects strips that are inputs to the same effect type as the active strip.
   :Time Overlap:
      Selects strips on any channel whose time range overlaps the active strip.
   :Visual Overlap:
      Selects strips on channels below the active strip's channel whose time range overlaps,
      plus their full effect chains.

Extend
   Adds matching strips to the current selection.
   When disabled, the existing selection is cleared before selecting matching strips.

Same Channel
   Only selects matching strips on the same channel as the active strip.
   This option only applies when the operator is invoked from the timeline.


.. _bpy.ops.sequencer.select_linked:

Select Linked
=============

.. reference::

   :Menu:      :menuselection:`Select --> Select Linked`
   :Shortcut:  :kbd:`Ctrl-L`

Selects neighboring strips linked to the current selection.


Side of Frame
=============

.. reference::

   :Menu:      :menuselection:`Select --> Side of Frame`

.. _bpy.ops.sequencer.select_side_of_frame:

Selects strips based on their position relative to the current frame.

Left :kbd:`[`
   Selects strips that lie completely to the left of the current frame.
Right :kbd:`]`
   Selects strips that lie completely to the right of the current frame.
Current
   Selects strips that intersect the current frame.


.. _bpy.ops.sequencer.select_handles:

Select Handles
==============

.. reference::

   :Menu:      :menuselection:`Select --> Handle`

Selects handles of the currently selected strips.

Both
   Selects both handles.
Left
   Selects the left handle.
Right
   Selects the right handle.
Both Neighbor
   Selects the handles of neighboring strips on both sides of the selected strips.
Left Neighbor
   Selects the handle of the neighboring strip to the left of the selected strips.
Right Neighbor
   Selects the handle of the neighboring strip to the right of the selected strips.


.. _bpy.ops.sequencer.select_side:

Select Channel
==============

.. reference::

   :Menu:      :menuselection:`Select --> Channel`

Selects all the strips that are in the same channels as the currently selected strips.
