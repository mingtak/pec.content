# -*- coding: utf-8 -*-
from pec.content import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides
import datetime
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


        header = request.file.readline()
        with open('/tmp/%s' % request.file.filename, 'wb') as file:
            file.write(request.file.read())

        # 確認檔頭(Header)正確性
        try:
            if not (header.split(',')[0].split('-')[0].isdigit() and header.split(',')[0].split('-')[1].isdigit()):
                api.portal.show_message(message=_(u'Wrong! please check file header.'), request=request, type='error')
                return self.template()
        except:
            api.portal.show_message(message=_(u'Wrong! please check file header.'), request=request, type='error')
            return self.template()

        with open('/tmp/%s' % request.file.filename, 'rb') as file:
            items = csv.DictReader(file) 
            fieldnames = items.fieldnames
#            fieldnames = csv.DictReader(file).fieldnames
            correctField = ['no.', 'class', 'id', 'name', 'age', 'gender', 'height', 'weight', 'running800', 'forward bend', 'long jump', 'sit-ups']

            # 確認欄位正確性
            try:
                for i in range(len(fieldnames)):
                    if correctField[i] != fieldnames[i]:
                        api.portal.show_message(message=_(u'Wrong! please check field names.'), request=request, type='error')
                        return self.template()
            except:
                api.portal.show_message(message=_(u'Wrong! please check field names.'), request=request, type='error')
                return self.template()

            # 格式正確，讀檔
#            items = csv.DictReader(file) #.fieldnames






            # check Folder content
            phfitFolder = portal.get('phfit')
            if not phfitFolder:
                api.portal.show_message(message=_(u'Error! please contact Admin to fix this problem.'), request=request, type='error')
                return self.template()

            header = header.split(',')
            folder = phfitFolder.get(header[0])
            if not folder:
                folder = api.content.create(
                    type='Folder',
                    container=phfitFolder,
                    id=header[0],
                    title='%s 學年度第 %s 學期體適能' % (header[0].split('-')[0], header[0].split('-')[1]),
                )

            # import csv item
#            import pdb; pdb.set_trace()
            for item in items:
                if True:
#                try:
                    id = item['id']
                    name = item['name']
                    whichClass = header[2]
                    age = int(item['age'])
                    gender = True if '男' in item['gender'] else False
                    height = float(item['height'])
                    weight = float(item['weight'])
                    minutes = int(item['running800'].split(':')[0])
                    seconds = int(item['running800'].split(':')[1])
                    running800 = datetime.timedelta(minutes=minutes, seconds=seconds)
                    forwardBend = float(item['forward bend'])
                    longJump = float(item['long jump'])
                    sitUps = int(item['sit-ups'])
                    bmi = weight/((height/100)*(height/100))

                    api.content.create(
                        container=folder,
                        type='PhFit',
                        id=id,
                        title=name,
                        whichClass=whichClass,
                        age=age,
                        gender=gender,
                        height=height,
                        weight=weight,
                        running800=running800,
                        forwardBend=forwardBend,
                        longJump=longJump,
                        sitUps=sitUps,
                        bmi=bmi,
                    )
#                except:
#                    api.portal.show_message(message='Error! data: %s' % str(item), request=request, type='error')
#                    return self.template()



#        import pdb; pdb.set_trace()
        api.portal.show_message(message='Import data finish.', request=request, type='info')
        return self.template()
