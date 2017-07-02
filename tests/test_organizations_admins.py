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

    def test_organization_admins_index(self):
        """ The organizations.admins.index endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/admins"
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .admins()
            .lazy()
            .index()
            .get_url()
        )

    def test_organization_admins_show(self):
        """ The organizations.admins.show endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/admins/"
            + ADMIN_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .admins(ADMIN_ID)
            .lazy()
            .show()
            .get_url()
        )

    def test_organization_admins_create(self):
        """ The organizations.admins.create endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/admins"
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .admins()
            .lazy()
            .create({})
            .get_url()
        )

    def test_organization_admins_update(self):
        """ The organizations.admins.update endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/admins/"
            + ADMIN_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .admins(ADMIN_ID)
            .lazy()
            .update({})
            .get_url()
        )

    def test_organization_admins_delete(self):
        """ The organizations.admins.delete endpoint should be correct. """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/admins/"
            + ADMIN_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .admins(ADMIN_ID)
            .lazy()
            .delete()
            .get_url()
        )

if __name__ == '__main__':
    unittest.main()
