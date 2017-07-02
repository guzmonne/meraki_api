"""
Meraki API
"""
from .meraki_api_resource import MerakiAPIResource
from .devices import Devices
from .organizations import Organizations
from .networks import Networks


class MerakiAPI(MerakiAPIResource):
    """ Meraki API class helper """

    def __init__(self, key):
        if key is None:
            raise ValueError("The 'key' value must be defined.")
        MerakiAPIResource.__init__(self, key)

    def organizations(self, organization_id=None):
        """ Returns an API Organization Resource. """
        return Organizations(self.key, None, organization_id)

    def networks(self, network_id=None):
        """ Returns an API Network Resource. """
        return Networks(self.key, None, network_id)

    def devices(self, serial=None):
        """ Returns an API Device Resource. """
        return Devices(self.key, None, serial)
