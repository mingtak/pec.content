# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from pec.content import _
from zope import schema
from zope.interface import Interface
from plone.namedfile.field import NamedBlobImage
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPecContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPhFit(Interface):
    """ Physical Fitness """
    title = schema.TextLine(
        title=_(u"Name"),
        required=True,
    )

    height = schema.Float(
        title=_(u"Height, cm"),
        required=True,
    )

    weight = schema.Float(
        title=_(u"Weight, kg"),
        required=True,
    )

    running800 = schema.Timedelta(
        title=_(u"Timedelta"),
        required=True,
    )

    forwardBend = schema.Float(
        title=_(u"Forward bend"),
        required=True,
    )

    sitUps = schema.Int(
        title=_(u"Sit-Ups with 60 seconds"),
        required=True,
    )

    longJump = schema.Float(
        title=_(u"Standing Long Jump"),
        required=True,
    )

    bmi = schema.Float(
        title=_(u"Body mass index(BMI)"),
        required=True,
    )


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
