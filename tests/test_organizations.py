"""
Meraki API Testing module.
"""

import unittest
# The context.py file on this folder sets up the context for the test case.
from context import MerakiAPI

KEY = "SOME_KEY"
ORGANIZATION_ID = 1234

class TestMerakiApi(unittest.TestCase):
    """ Meraki API test case. """

    def test_organizations_index(self):
        """ The organizations.index endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations",
            MerakiAPI(KEY).organizations().lazy().index().cached.url
        )

    def test_organizations_show(self):
        """ The organizations.show enpoint. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .show()
            .cached
            .url
        )

    def test_organizations_create(self):
        """ Tes organizations.create endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations"
            , MerakiAPI(KEY)
            .organizations()
            .lazy()
            .create({})
            .cached
            .url
        )

    def test_organizations_update(self):
        """ The organizations.update enpoint. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .update({})
            .cached
            .url
        )

    def test_organizations_delete(self):
        """ The organizations.delete enpoint. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .delete()
            .cached
            .url
        )

    def test_organizations_clone(self):
        """ The organizations.clone endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            + "/clone",
            MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .clone({})
            .cached.url
        )

    def test_organizations_claim(self):
        """ The organizations.claim endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            + "/claim",
            MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .claim({})
            .cached.url
        )

    def test_organizations_licenseState(self):
        """ The organizations.licenseState endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            + "/licenseState",
            MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .license_state()
            .cached.url
        )

    def test_organizations_inventory(self):
        """ The organizations.inventory endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            + "/inventory",
            MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .inventory()
            .cached.url
        )

    def test_organizations_snmp(self):
        """ The organizations.snmp endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            + "/snmp",
            MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .snmp()
            .cached.url
        )

    def test_organizations_thirdPartyVPNPeers(self):
        """ The organizations.thirdPartyVPNPeers endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            + "/thirdPartyVPNPeers",
            MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .third_party_vpn_peers()
            .cached.url
        )

    def test_organizations_updateThirdPartyVPNPeers(self):
        """ The organizations.thirdPartyVPNPeers endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + str(ORGANIZATION_ID)
            + "/thirdPartyVPNPeers",
            MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .lazy()
            .update_third_party_vpn_peers({})
            .cached.url
        )

if __name__ == '__main__':
    unittest.main()
