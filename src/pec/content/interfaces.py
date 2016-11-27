# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from pec.content import _
from zope import schema
from zope.interface import Interface
from plone.namedfile.field import NamedBlobImage
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

    hvStartSecond = schema.Int(
        title=_(u"Hero Video Start Second"),
        default=0,
        required=True,
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


    image = NamedBlobImage(
        title=_(u"Profile Image"),
        required=False,
    )
