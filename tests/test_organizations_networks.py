"""
Meraki API Testing module.
"""

KEY = "SOME_KEY"
ORGANIZATION_ID = "ORGANIZATION_ID"
NETWORK_ID = "NETWORK_ID"

import unittest
# The context.py file on this folder sets up the context for the test case.
from context import MerakiAPI

class TestMerakiApi(unittest.TestCase):
    """ Meraki API test case. """

    def test_organization_networks_index(self):
        """ The organizations.networks.index endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/networks"
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .networks()
            .lazy()
            .index()
            .cached
            .url
        )

    def test_organization_networks_show(self):
        """ The organizations.networks.show endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/networks/"
            + NETWORK_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .networks(NETWORK_ID)
            .lazy()
            .show()
            .cached
            .url
        )

    def test_organization_networks_create(self):
        """ The organizations.networks.create endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/networks"
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .networks()
            .lazy()
            .create({})
            .cached
            .url
        )

    def test_organization_networks_update(self):
        """ The organizations.networks.update endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/networks/"
            + NETWORK_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .networks(NETWORK_ID)
            .lazy()
            .update({})
            .cached
            .url
        )

    def test_organization_networks_delete(self):
        """ The organizations.networks.delete endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/networks/"
            + NETWORK_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .networks(NETWORK_ID)
            .lazy()
            .delete()
            .cached
            .url
        )

    def test_organization_networks_traffic(self):
        """ The organizations.networks.traffic endpoint should be correct. """
        req = MerakiAPI(KEY).organizations(ORGANIZATION_ID).networks(NETWORK_ID).lazy().traffic({
                "timespan": 7200,
                "deviceType": "wireless"
            })

        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/networks/"
            + NETWORK_ID
            + "/traffic"
            , req
            .cached
            .url
        )
        self.assertEqual(
            {'deviceType': 'wireless', 'timespan': 7200}
            , req
            .cached
            .data
)

if __name__ == '__main__':
    unittest.main()
