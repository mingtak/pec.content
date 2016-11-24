# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from pec.content.testing import PEC_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that pec.content is properly installed."""

    layer = PEC_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pec.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'pec.content'))

    def test_browserlayer(self):
        """Test that IPecContentLayer is registered."""
        from pec.content.interfaces import (
            IPecContentLayer)
        from plone.browserlayer import utils
        self.assertIn(IPecContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PEC_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['pec.content'])

    def test_product_uninstalled(self):
        """Test if pec.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'pec.content'))

    def test_browserlayer_removed(self):
        """Test that IPecContentLayer is removed."""
        from pec.content.interfaces import IPecContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPecContentLayer, utils.registered_layers())
