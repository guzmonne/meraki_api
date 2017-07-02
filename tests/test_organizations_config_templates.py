"""
Meraki API Testing module.
"""

KEY = "SOME_KEY"
ORGANIZATION_ID = "ORGANIZATION_ID"
CONFIG_TEMPLATE_ID = "CONFIG_TEMPLATE_ID"

import unittest
# The context.py file on this folder sets up the context for the test case.
from context import MerakiAPI

class TestMerakiApi(unittest.TestCase):
    """ Meraki API test case. """

    def test_organization_config_templates_index(self):
        """
        The organizations.config_templates.index endpoint should be correct.
        """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/configTemplates"
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .config_templates()
            .lazy()
            .index()
            .cached
            .url
        )

    def test_organization_config_templates_show(self):
        """
        The organizations.config_templates.show endpoint should be correct.
        """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/configTemplates/"
            + CONFIG_TEMPLATE_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .config_templates(CONFIG_TEMPLATE_ID)
            .lazy()
            .show()
            .cached
            .url
        )

    def test_organization_config_templates_create(self):
        """
        The organizations.config_templates.create endpoint should be correct.
        """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/configTemplates"
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .config_templates()
            .lazy()
            .create({})
            .cached
            .url
        )

    def test_organization_config_templates_update(self):
        """
        The organizations.config_templates.update endpoint should be correct.
        """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/configTemplates/"
            + CONFIG_TEMPLATE_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .config_templates(CONFIG_TEMPLATE_ID)
            .lazy()
            .update({})
            .cached
            .url
        )

    def test_organization_config_templates_delete(self):
        """
        The organizations.config_templates.delete endpoint should be correct.
        """
        self.assertEqual(
            "https://dashboard.meraki.com/api/v0/organizations/"
            + ORGANIZATION_ID
            + "/configTemplates/"
            + CONFIG_TEMPLATE_ID
            , MerakiAPI(KEY)
            .organizations(ORGANIZATION_ID)
            .config_templates(CONFIG_TEMPLATE_ID)
            .lazy()
            .delete()
            .cached
            .url
        )

if __name__ == '__main__':
    unittest.main()
