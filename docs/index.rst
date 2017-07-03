.. meraki_api documentation master file, created by
   sphinx-quickstart on Sun Jul  2 18:31:42 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MerakiAPI's documentation!
=====================================

.. module:: meraki_api

MerakiAPI is a Python wrapper to better interact with the Meraki Dashboard API.

Its main advantages are:

* Chainable API to interact with all the API endpoints.
* All endpoints can be called lazily (first defined and called later.)
* Handles the authorization key.
* Sets the needed headers.
* Returns `requests` response object.

This module has all the endpoints exposed as of the 1 of July 2017. You can find
more information about the API at its 
`official website <https://dashboard.meraki.com/api_docs>`_.

MerakiAPI usage example
-----------------------

To use this module you only have to import the `MerakiAPI` class, and 
instantiate a new instance of it, passing your profile access token. Then we can
use its chainable api to call the different endpoints provided by the API.::

    from meraki_api import MerakiAPI

    KEY = "YOUR_PROFILE_AUTHORIZATION_KEY"

    meraki = MerakiAPI(KEY)

    # Here is the code to get a list of all the organizations we have access to.
    response = meraki.organizations().index()

    # It returns a `requests` response object. We can get its content by calling
    # `.json()` on it.
    organizations = response.json()
    
    # To get just the information of a specific organization we must pass its id
    # when getting the organizations resource. Then we call `show()` on it to 
    # get its current details.
    organization_key = "ORGANIZATION_KEY"
    organization_resource = meraki.organizations(organization_key)
    organization_details = organization_resource.show().json()

    # We can also update the organization details using the previously defined
    # organization resource.
    organization_resource.update({"name": "New organization name."})

.. note::

  You need the `requests` module in order for this API to work. Actually, this
  module does very little compared to what `requests` does.

Contents
--------

.. toctree::
    :maxdepth: 2

    meraki_api
    meraki_api_resource
    faq

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
