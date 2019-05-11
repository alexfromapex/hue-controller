#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import globals
import sys

def ask(parent=None, message='', default_value=''):
    dlg = wx.TextEntryDialog(parent, message, value=default_value)
    option = dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    if option == wx.ID_OK:
        return result
    return False


def scrollHandler(event, light_id):
    try:
        brightness = event.GetPosition()
        if brightness is not 0:
            globals.b.set_light(light_id,'on',True)
            globals.b.set_light(light_id,'bri',brightness)
        else:
            globals.b.set_light(light_id,'on',False)
    except Exception:
        print(sys.exc_info())
        # print repr(Exception)
