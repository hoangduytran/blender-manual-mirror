
**************
Brush Settings
**************

.. reference::

   :Mode:      Sculpt Mode
   :Panel:     :menuselection:`Sidebar --> Tool --> Brush Settings`

Size
   This option controls the size of the brush, measured in pixels.
   :kbd:`F` allows you to change the brush size interactively by
   dragging the mouse from left to right and then :kbd:`LMB` to accept.
   Meanwhile the texture of the brush will be visible inside the circle.
   You can also enter the size numerically with the number keys.

   The size can be decreased/increased using :kbd:`[` and :kbd:`]` respectively.

   :bl-icon:`stylus_pressure` (Size Pressure)
      Adjusts the size based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.
   :bl-icon:`brushes_all` (Use Unified Size)
      Use the shared brush *Size* value for this brush.
   :bl-icon:`rightarrow` / :bl-icon:`downarrow_hlt` (Expand/Collapse)
      Show or hide the customizable pressure curve.

      Custom Curve
         By default this is a straight line with positive slope such that
         increased pressure results in a larger brush size.

         For the curve controls see: :ref:`Curve widget <ui-curve-widget>`.

Strength
   For painting brushes the *Strength* defines the maximum effect of each brush stroke.
   For example, higher values cause a *Paint* brush to give each stroke a higher opacity.
   The opacity is never stronger than the set *Strength*,
   no matter how often the same surface is painted during the same stroke.

   For sculpting brushes on the other hand the *Strength* relates to how strong each step of the stroke is,
   resulting in a slower/faster buildup towards the full brush effect during the stroke.

   You can change the brush strength interactively by pressing :kbd:`Shift-F`
   and then moving the brush and then :kbd:`LMB`.
   You can also enter the strength numerically with the number keys.

   :bl-icon:`stylus_pressure` (Strength Pressure)
      Adjusts the strength based on the stylus pressure when using a :ref:`Graphics Tablet <hardware-tablet>`.
   :bl-icon:`brushes_all` (Use Unified Strength)
      Use the shared brush *Strength* value for this brush.
   :bl-icon:`rightarrow` / :bl-icon:`downarrow_hlt` (Expand/Collapse)
      Show or hide the customizable pressure curve.

      Custom Curve
         By default this is a straight line with positive slope such that
         increased pressure results in a stronger brush deformation.

         For the curve controls see: :ref:`Curve widget <ui-curve-widget>`.

.. note::

   The following *Affect* settings are only available for *Smooth* and *Randomize* brushes.

.. _bpy.types.BrushGpencilSettings.use_edit_position:

Affect -- Position
   Toggles the brush effect on the position of the stroke points.

.. _bpy.types.BrushGpencilSettings.use_edit_strength:

Affect -- Strength
   Toggles the brush effect on the strength (alpha) of the stroke points.

.. _bpy.types.BrushGpencilSettings.use_edit_thickness:

Affect -- Thickness
   Toggles the brush effect on the thickness of the stroke points.

.. _bpy.types.BrushGpencilSettings.use_edit_uv:

Affect -- UV
   Toggles the brush effect on the UV rotation of the stroke points.


Falloff
=======

See the global brush settings for :doc:`Falloff </sculpt_paint/brush/falloff>` settings.


Cursor
======

See the global brush settings for :doc:`Cursor </sculpt_paint/brush/cursor>` settings.
