#!/usr/bin/python

import wx
from phue import Bridge
import random
import time
import sys
import signal
from threading import Thread
import threading

b = Bridge('192.168.1.76')
lights = b.get_light_objects('id')

def lightFunc(self):
    try:
        b.set_light(lights, 'bri', 254)
        for light_id in lights:
            color1 = random.random()
            color2 = random.random()
            name = b.get_light(light_id,'name')
            print name,':'
            print color1,color2
            b.set_light(light_id, 'xy',[color1,color2])
    except KeyboardInterrupt:
        sys.exit(0)

def allOn(self):
    try:
        b.set_light(lights,'on',True)
    except KeyboardInterrupt:
        sys.exit(1)

def scrollHandler(self):
    try:
        b.set_light(1,'bri',self.GetPosition())
    except Exception:
        print Exception

class Frame(wx.Frame):
    def __init__(self,l_thread):
        self._light_thread = l_thread
        wx.Frame.__init__(self, None, title='Hue Controller', size=(800,500))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        menuBar.Append(menu, "&File")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        self.SetMenuBar(menuBar)

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        
        btn_rand_clr = wx.Button(panel, wx.ID_ANY, "Random Colors")
        btn_rand_clr.Bind(wx.EVT_BUTTON, lightFunc)
        
        btn_turn_all_on = wx.Button(panel, wx.ID_ANY, "Turn All Lights On")
        btn_turn_all_on.Bind(wx.EVT_BUTTON, allOn)

        label1 = wx.StaticText(panel, label=b.get_light(1,'name')+": ")
        hslider = wx.Slider(panel, -1, b.get_light(1,'bri'), 0, 254,
            size=(250, -1),
            style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
        hslider.SetTickFreq(5, 1)
        hslider.Bind(wx.EVT_SCROLL, scrollHandler)
        
        box.Add(btn_rand_clr, 0, wx.ALL, 10)
        box.Add(btn_turn_all_on, 0, wx.ALL, 10)
        box.Add(label1, 0, wx.ALL, 10)
        box.Add(hslider, 0, wx.ALL, 10)
        panel.SetSizer(box)
        panel.Layout()
        self.Show()

    def OnClose(self,event):
        self._light_thread.stop()
        self.Destroy()

class LightThread(threading.Thread):
    def __init__(self,function_name):
        super(LightThread, self).__init__()
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

if __name__=='__main__':
    try:
        light_thread = LightThread(lightFunc)
        app=wx.App(False)
        frame=Frame(light_thread)
        app.MainLoop()
    except KeyboardInterrupt:
        light_thread.stop()
        sys.exit(0)
