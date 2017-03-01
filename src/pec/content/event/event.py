# -*- coding: utf-8 -*-
from plone import api


def moveContentToTop(item, event):
    """ Moves Item to the top of its folder """
    folder = item.getParentNode()
    if not hasattr(folder, 'moveObjectsToTop'):
        return

    folder.moveObjectsToTop(item.id)
