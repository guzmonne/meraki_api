"""
Meraki API Testing module.
"""

KEY = "SOME_KEY"
ORGANIZATION_ID = "ORGANIZATION_ID"
ADMIN_ID = "ADMIN_ID"

import unittest
# The context.py file on this folder sets up the context for the test case.
from context import MerakiAPI

class TestMerakiApi(unittest.TestCase):
    """ Meraki API test case. """

    def test_organization_samlRoles_index(self):
        """ The organizations.samlRoles.index endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/samlRoles"
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .saml_roles()
            .lazy()
            .index()
            .cached
            .url
        )

    def test_organization_samlRoles_show(self):
        """ The organizations.samlRoles.show endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/samlRoles/"
            + ADMIN_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .saml_roles(ADMIN_ID)
            .lazy()
            .show()
            .cached
            .url
        )

    def test_organization_samlRoles_create(self):
        """ The organizations.samlRoles.create endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/samlRoles"
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .saml_roles()
            .lazy()
            .create({})
            .cached
            .url
        )

    def test_organization_samlRoles_update(self):
        """ The organizations.samlRoles.update endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/samlRoles/"
            + ADMIN_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .saml_roles(ADMIN_ID)
            .lazy()
            .update({})
            .cached
            .url
        )

    def test_organization_samlRoles_delete(self):
        """ The organizations.samlRoles.delete endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/samlRoles/"
            + ADMIN_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .saml_roles(ADMIN_ID)
            .lazy()
            .delete()
            .cached
            .url
        )

if __name__ == '__main__':
    unittest.main()
