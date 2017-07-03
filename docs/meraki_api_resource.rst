MerakiAPIResource
=================

Base class that all further endpoints inherits from. Each endpoint overrides it
with its own custom endpoints, using the functions inherited from each class.
Also, each *child* class must override the `resource` and `parameters` variable.

.. autoclass:: meraki_api.MerakiAPIResource
   :members:
