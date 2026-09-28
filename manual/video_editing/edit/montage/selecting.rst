
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


.. _bpy.ops.sequencer.select_grouped:

Select Grouped
==============

.. reference::

   :Menu:      :menuselection:`Select --> Select Grouped`
   :Shortcut:  :kbd:`Shift-G`

Selects strips that are similar to the active strip. By default, unsimilar strips are deselected,
but this can be changed in the :ref:`Adjust Last Operation <bpy.ops.screen.redo_last>` region.

Type
   Selects strips that have the same specific type as the active strip.
   For example, if the active strip is a Movie strip, this selects all Movie strips.
Global Type
   Selects strips that have the same general type (graphics or audio) as the active strip.
Effect Type
   If the active strip is an effect strip, selects all effect strips.
   Otherwise, selects all non-effect strips.
   Despite the name, this operator does not check the effect type.
Data
   Selects strips that use the same source (file, scene, movie clip or mask) as the active strip.
Effect
   Finds the effect types that are applied to the active strip, and selects all strips that have
   any of the same effect types applied to them. For example, if the active strip has a
   Gaussian Blur effect on it, this selects all other strips that are also blurred.
Effect/Linked
   Selects strips that are on a lower channel than a selected strip and overlap it in time;
   then, effect strips linked to the selected content strips; and finally, content strips
   linked to the selected effect strips.
Overlap
   Selects strips that partially or completely overlap the active strip in time.


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
