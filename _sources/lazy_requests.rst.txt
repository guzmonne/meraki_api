LazyRequests
============

This class provides a set of functions to interact with the `requests` library.
It can *cache* a `requests` invocation for latter use, or call it immediately.
This behaviour allows to check the the url of the request before calling it or
to instantiate requests to call them in parallel later.

.. autoclass:: meraki_api.LazyRequests
   :members:
