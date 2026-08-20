
******
Bundle
******

A *bundle* is a container that groups multiple values into one socket.
This makes it possible to pass many values through
a single link, similar to a *struct* in programming.

Bundles reduce the number of exposed inputs and outputs in a node group,
and can contain mixed data types such as geometry, fields, values, objects,
or even nested bundles.

.. --- section-nodes ---

Nodes
=====

The following nodes are provided for working with bundles:

.. toctree::
   :maxdepth: 1

   combine_bundle.rst
   separate_bundle.rst

-----

.. toctree::
   :maxdepth: 1

   get_bundle_item.rst
   store_bundle_item.rst

-----

.. toctree::
   :maxdepth: 1

   Typed Bundle <typed_bundle.rst>
