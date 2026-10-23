.. _projects-variables:

*****************
Project Variables
*****************

Project Variables are name-value pairs that can be used just like :ref:`built-in
Blender Variables <files-built_in_variables>` within any blend file in the
project.  Like built-in Blender Variables, at the moment they can only be used
within :ref:`Path Templates <files-path_templates>`.

Built-In Project Variables
==========================

Whenever you're within a project, the following built-in project variables are
automatically available:

:``project_name``: The name of the current project.
:``project_root``: The absolute filepath of the project's root directory.

Custom Project Variables
========================

You can also create your own custom project variables within a project.

Go to :menuselection:`Project --> Settings... --> Variables`:

.. figure:: /images/projects_project_settings_variables.png

Here you can add and remove variables, and edit their names, values, etc.

Type
----

Variables have three main types:

:String: A variable for string values.
:Integer: A variable integer number values.
:Float: A variable for number values with fractional components.

.. note::

   A variable's type is fixed at creation time, and cannot be changed
   afterwards.  If you wish to change a variable's type you must delete it and
   create a new variable of the desired type to replace it.

Subtype
-------

String variables additionally have a subtype:

:None: A normal string.
:Filepath: A filepath, whose value is passed through as-is in a filepath context
   (such as in path templates).

For example, if the String variable's value is "Left/Right", then in a path
template the slash will be left as-is if the variable's subtype is Filepath, but
will be replaced so it won't be interpreted as a filepath separator if the
subtype is None.

Name
----

A variable's name is how the variable is referenced elsewhere in Blender. For
example, if a variable's name is ``foo``, then inside a path template you would
write ``{foo}`` to use it.

Variable names are restricted to alphanumeric characters and underscores, and
must not start with a numeric character.

Variable names must be unique within the list of Project Variables.

Value
-----

The value of the variable, which is used wherever the variable is referenced.

For example, if you have a variable named ``foo`` with the value "Suzanne is
great", then a path template "hi-{foo}-bye" will become "hi-Suzanne is
great-bye".

Description
-----------

An optional description of the variable's purpose or meaning. This has no
functional impact, but is useful for documenting a project's custom variables.
