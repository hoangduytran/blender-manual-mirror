
***************
Copy/Paste Pose
***************

Blender allows poses to be copied between armatures using a temporary pose buffer.
Poses can be pasted normally or mirrored across the X axis.


.. _bpy.ops.pose.copy:

Copy Pose
=========

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Copy Pose`
   :Shortcut:  :kbd:`Ctrl-C`

Copies the pose of the selected bones to the pose buffer.
Only selected bones are included, allowing individual parts of a pose to be copied.


.. _bpy.ops.pose.paste:

Paste Pose
==========

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Paste Pose`
   :Shortcut:  :kbd:`Ctrl-V`

Pastes the buffered pose onto the current armature.

Bones are matched by name, regardless of their selection state.
Only bones with matching names receive the copied transforms.


Paste Pose Flipped
==================

.. reference::

   :Mode:      Pose Mode
   :Menu:      :menuselection:`Pose --> Paste Pose Flipped`
   :Shortcut:  :kbd:`Shift-Ctrl-V`

Pastes the buffered pose mirrored across the X axis.

This is useful for transferring poses between the left and right sides of an armature,
such as copying the pose of one arm to the other.


How Copy/Paste Works
====================

The pose buffer has the following characteristics:

- The buffer is shared across the entire :term:`Blender session`,
  allowing poses to be copied between armatures, scenes, and blend-files.
  However, the buffer is not saved and is cleared when Blender closes.
- Only one pose can be stored in the buffer at a time.
  Copying another pose replaces the previous contents.
- Only selected bones are copied, but bone selection is ignored when pasting.
  Instead, the copied transforms are applied to bones with matching names.
- The copied transforms include each bone's location, rotation, and scale
  relative to its own space.

Because transforms are stored in each bone's local space, the resulting pose
may differ from the original depending on:

- The rest position of the bones.
- The current pose of their parent bones.


Examples
========

.. list-table::

   * - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-1.png

          The rest position of the original armature.

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-2.png

          The rest position of the destination armature.

.. list-table:: Examples of pose copy/paste.

   * - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-3.png

          The first copied pose (only two bones are selected and copied).

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-4.png

          The pose pasted onto the destination armature.

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-5.png

          The mirrored pose pasted onto the destination armature.

   * - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-6.png

          The same pose is copied, this time with all bones selected.

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-7.png

          The pose pasted onto the destination armature.

     - .. figure:: /images/animation_armatures_posing_editing_copy-paste_examples-8.png

          The mirrored pose pasted onto the destination armature.
