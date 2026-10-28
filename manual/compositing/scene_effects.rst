
.. _compositor-scene-effects:

*************
Scene Effects
*************

The *Layered Compositor* allows compositing effects to be applied to a scene
using an ordered stack of node groups. Each effect processes the image produced
by the previous effect, making it possible to build complex compositing
setups from smaller, reusable components.

This workflow is similar to the :doc:`Modifier Stack </modeling/modifiers/introduction>`,
where each modifier processes the result of the preceding modifier.

Each effect can be independently enabled or disabled for viewport previews
and final rendering, allowing different compositing setups to be tested
without modifying the underlying node groups.


How Scene Effects Work
======================

Each Scene Effect references a compositor node group that defines how the
image is processed.

The first effect receives the Combined render pass of the scene as its input.
Each subsequent effect receives the output of the preceding effect,
with the final effect producing the composited image.

For example, a stack might contain the following effects:

#. **Exposure:** Adjusts the brightness of the rendered image.
#. **Bloom:** Adds a glow around bright areas.
#. **Vignette:** Darkens the edges of the image.
#. **Color Grading:** Adjusts the final colors and contrast.

The effects are evaluated in stack order, so changing their order can
change the resulting image.

Unlike a single large node tree, individual effects can be reused,
reordered, or disabled without changing the other effects.


Managing Scene Effects
======================

Scene Effects are managed in the *Compositor* tab of the Properties editor.

The effects list displays the compositing effects assigned to the active scene.
Each effect references a compositor node group, which can be edited in the
:doc:`Compositor </editors/compositor>`.

Effects can be added, removed, duplicated, and reordered to build
the desired compositing stack.

The active effect determines which node group is displayed in the
Compositor editor.


.. _bpy.ops.scene.add_compositor_effect_node_group_asset:
.. _bpy.ops.scene.new_compositor_effect_node_group:

Adding Effects
--------------

Scene Effects can be created using existing compositor node groups or
assets designed for use as Scene Effects.

Compositor node groups can be marked as Scene Effect assets,
allowing them to be reused across different scenes and projects.

This makes it possible to build a library of common effects,
such as bloom, color correction, blur, and other image adjustments.


Reordering Effects
------------------

The order of effects determines how the image is processed.
Each effect receives the result of the preceding effect,
so moving an effect changes where it is applied in the compositing pipeline.

For example, applying a blur before a color adjustment may produce
a different result than applying the blur afterward.


.. _bpy.types.SceneCompositorEffect.enable_for_preview:

Enabling and Disabling Effects
------------------------------

Each effect has independent controls for enabling or disabling its
evaluation in viewport previews and final renders.

This allows effects to be temporarily bypassed while editing,
or excluded from final rendering without removing them from the stack.

Disabling an effect passes the previous effect's result to the next
enabled effect.



Editing Scene Effects
=====================

Selecting an effect in the stack displays its compositor node group
in the Compositor editor.

The node group defines how the effect processes its input image.
The :doc:`Group Input Node </compositing/types/groups>`
provides the image from the preceding effect,
or the Combined render pass when the effect is first in the stack.

The processed image is passed to the next effect through the
:doc:`Group Output Node </compositing/types/groups>`.

This allows each effect to be edited independently while remaining
part of the overall compositing pipeline.


Previewing Effects
==================

The :doc:`Viewer Node </compositing/types/output/viewer>` can be used
to preview the result of an effect while editing its node group.

Only Viewer nodes belonging to the active effect are considered active.
If the active effect has no active Viewer node, the preview falls back
to the final output of the entire effects stack.

This allows individual effects to be inspected without changing
the final compositing result.
