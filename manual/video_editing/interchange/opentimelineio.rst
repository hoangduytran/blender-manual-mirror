
**************
OpenTimelineIO
**************

:abbr:`OpenTimelineIO (OTIO)` is an open-source format for exchanging
video editing timelines between applications.

Blender supports importing and exporting OpenTimelineIO (``.otio``) files,
allowing edits to be transferred between the Video Sequencer and other
compatible video editing applications.

OpenTimelineIO stores the structure of an edit, including clip timing,
track organization, and references to source media. The media files
themselves are not embedded in the exported timeline.

.. seealso::

   `OpenTimelineIO Documentation <https://opentimelineio.readthedocs.io/>`__


Import
======

Imports an OpenTimelineIO file into the Video Sequencer, converting supported
timeline elements into strips.

The imported timeline preserves the timing and organization of the original edit,
including track names, channel assignments, and mute and lock states where supported.

The timeline's frame rate and global start time are used to set the scene's
frame rate and start frame.

If the current Sequencer scene already contains strips, a new scene is created
for the imported timeline to avoid modifying the existing edit.

When importing from the Video Sequencer, Blender automatically switches to
the destination scene. Otherwise, the import is performed without switching
scenes, and the destination scene is reported.

Multiple OpenTimelineIO files can be imported at once.
Files can also be imported by dragging and dropping them into the Video Sequencer.

.. note::

   The original media files must remain accessible for the imported
   strips to display correctly.


Metadata
--------

Blender-specific metadata is restored to the corresponding scene and strip
properties where supported. This includes information needed to reconstruct
the original Video Sequencer timeline, such as channel assignments.

Metadata from other editing applications is interpreted where possible.
Unrecognized metadata is preserved as custom properties on the scene or strips,
allowing it to be retained when exporting the timeline again.

Some timeline elements and application-specific features may not be fully
supported when importing files created by other video editing applications.


Export
======

Exports the Video Sequencer timeline to an OpenTimelineIO file,
allowing the edit to be transferred to other compatible video editing applications.

The exported file contains the timeline structure, strip timing,
track organization, and references to source media.

Video Sequencer channels containing both video and audio strips are exported
as separate video and audio tracks. The original channel assignments are
stored as metadata so they can be restored when importing the file back into Blender.


Metadata
--------

Blender-specific strip properties are stored as metadata in the exported file.
This allows information that is not directly supported by OpenTimelineIO
to be preserved when importing the timeline back into Blender.

Metadata from other editing applications that was preserved during import
is also included when exporting, allowing it to be retained across multiple
import and export operations.


Compatibility
-------------

Most strip types can be exported in a form recognized by other video editing applications.
However, some Video Sequencer features cannot be represented directly in OpenTimelineIO.

These include:

- Scene, Mask, Movie Clip, Multicam, and Compositor strips.
- Image sequences with nonsequential frame numbering.
- Transitions whose input strips are on different channels.

These strips are still exported with Blender-specific metadata,
allowing them to be restored when the file is imported back into Blender,
provided the metadata has been preserved.

When unsupported strip types are encountered, Blender reports a warning
indicating their types and the number of affected strips.

.. note::

   Unsupported strips may not be interpreted correctly by other video editing
   applications. Editing or reexporting the timeline in another application
   may also discard the Blender-specific metadata needed to restore these strips.


Options
-------

DaVinci Resolve Metadata
   Exports additional metadata recognized by DaVinci Resolve to improve
   compatibility when importing the timeline into that application.

   This metadata is used to represent certain timeline elements that
   are not directly supported by OpenTimelineIO.
