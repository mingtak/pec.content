# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class PHFitOverView(BrowserView):

    template = ViewPageTemplateFile("template/phfit_overview.pt")

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()

        id = request.form.get('id')
        personalId = request.form.get('personalId')

        if id and personalId:
            brain = api.content.find(context=portal, Type="PhFit", id=id)
            if brain:
                request.response.redirect('%s?id=%s&personalId=%s' % (brain[0].getURL(), id, personalId))

        return self.template()


class PhFitView(BrowserView):

    template = ViewPageTemplateFile("template/phfit_view.pt")

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()

        id = request.form.get('id')
        personalId = request.form.get('personalId')

        if id != context.id or personalId.lower() != context.personalId.lower():
            request.response.redirect('%s/phfit' % portal.absolute_url())


        return self.template()


class CoverView(BrowserView):

    template = ViewPageTemplateFile("template/cover_view.pt")

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()

        return self.template()


class MemberView(BrowserView):

    template = ViewPageTemplateFile("template/member_view.pt")

    def __call__(self):
        context = self.context
        request = self.request
        portal = api.portal.get()

        return self.template()

