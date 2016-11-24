# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import pec.content


class PecContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=pec.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pec.content:default')


PEC_CONTENT_FIXTURE = PecContentLayer()


PEC_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PEC_CONTENT_FIXTURE,),
    name='PecContentLayer:IntegrationTesting'
)


PEC_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PEC_CONTENT_FIXTURE,),
    name='PecContentLayer:FunctionalTesting'
)


PEC_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PEC_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PecContentLayer:AcceptanceTesting'
)
