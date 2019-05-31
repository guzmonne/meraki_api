"""
Meraki Clients API Resource
"""
import urllib
from .meraki_api_resource import MerakiAPIResource

class Clients(MerakiAPIResource):
    """ Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. """

    resource = "clients"

    def __init__(self, key, prefix=None, resource_id=None):
        MerakiAPIResource.__init__(self, key, prefix, resource_id)

    def traffic_history(self):
        """ Return the license state. """
        self.check_for_resource_id()
        return self.get("/trafficHistory")
