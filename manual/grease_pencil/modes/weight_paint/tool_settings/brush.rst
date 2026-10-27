.. _tool-grease-pencil-weight-paint-weight:

**************
Brush Settings
**************

Painting needs paint brushes and Blender provides a Brush panel within the Toolbar
when in *Weight Paint Mode*.

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

Weight :kbd:`Ctrl-F`
   The weight (visualized as a color) to be used by the brush.

   Using :kbd:`Ctrl-RMB` you can set the weight to the value that's under the cursor.

Direction :kbd:`D`
   Brush direction toggle, *Add* adds weight value while *Subtract* removes weight value.
   This setting can be toggled with :kbd:`D`.


Falloff
=======

See the global brush settings for :doc:`Falloff </sculpt_paint/brush/falloff>` settings.


Cursor
======

See the global brush settings for :doc:`Cursor </sculpt_paint/brush/cursor>` settings.
