# -*- coding: utf-8 -*-
from pec.content import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
import csv
import logging


class ImportPhFit(BrowserView):

    template = ViewPageTemplateFile("template/import_phfit.pt")

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()
        alsoProvides(request, IDisableCSRFProtection)

        if not request.form.get('file'):
            return self.template()

        if not request.file.filename.lower().endswith('.csv'):
            api.portal.show_message(message=_(u'Wrong! please upload a .csv file'), request=request, type='error')
            return self.template()

        return self.template()
