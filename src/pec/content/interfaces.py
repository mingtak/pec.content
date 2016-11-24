# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from pec.content import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPecContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICover(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    heroVideo = schema.URI(
        title=_(u"Hero Video"),
        required=False,
    )


class IMember(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    jobTitle = schema.TextLine(
        title=_(u"Job Title"),
        required=True,
    )
