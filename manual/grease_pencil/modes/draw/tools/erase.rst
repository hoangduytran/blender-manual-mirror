.. _tool-grease-pencil-draw-erase:

**********
Erase Tool
**********

.. reference::

   :Mode:      Draw Mode
   :Tool:      :menuselection:`Toolbar --> Brush`

The Erase tool erases already drawn strokes.

The Erase tool uses any of the Grease Pencil *Erase* draw mode brushes.
Activating a brush from an asset shelf or brush selector will also activate this tool for convenience.


Tool Settings
=============

Brush Asset
-----------

The asset selector can be used to open a pop-up asset browser to select the active brush asset for the tool.

See :ref:`brush-management-utility-operators` for more information.


Brush Settings
--------------

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

.. _bpy.types.BrushGpencilSettings.eraser_mode:

Mode
   Determines how the erase tool behaves.

   :Dissolve:
      To simulate a raster type eraser, this eraser type
      affects the strength and thickness of the strokes before actually delete a point.
   :Point: Delete one point at a time.
   :Stroke: Delete an entire stroke.


Cursor
^^^^^^

The cursor can be disabled by toggling the checkbox in the *Cursor* pop-over menu.


Usage
=====

Selecting a Brush
-----------------

In the Tool Settings select the brush to use with the tool.
The Erase tool uses :ref:`Erase Brush <grease_pencil-draw-brushes-erase>` types (soft, point and stroke).


Dissolve Erasing
----------------

- Select an erase brush of type Soft/Hard.
- Adjust brush settings.
- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-02.png
          :width: 200px

          The eraser affect the transparency of the strokes.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_soft-03.png
          :width: 200px

          Final result.


Point Erasing
-------------

- Select an erase brush of type Point.
- Adjust brush settings.
- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-02.png
          :width: 200px

          The eraser delete one point at a time.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_point-03.png
          :width: 200px

          Final result.


Stroke Erasing
--------------

- Select an erase brush of type Stroke.
- Adjust brush settings.
- Click and hold :kbd:`LMB` or use the :kbd:`Pen` tip to delete strokes on the viewport.

.. list-table::

   * - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-01.png
          :width: 200px

          Original drawing.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-02.png
          :width: 200px

          The eraser delete one stroke at a time.

     - .. figure:: /images/grease-pencil_modes_draw_tools_erase_stroke-03.png
          :width: 200px

          Final result.
