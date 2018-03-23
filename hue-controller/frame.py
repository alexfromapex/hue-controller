import wx
import globals
import ui
import wx.lib.scrolledpanel

class Frame(wx.Frame):
    def __init__(self,l_thread):
        self._light_thread = l_thread
        wx.Frame.__init__(self, None, title='Hue Controller', size=(800,600))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        menuBar.Append(menu, "&File")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        self.SetMenuBar(menuBar)

        panel = wx.lib.scrolledpanel.ScrolledPanel(self)
        panel.SetupScrolling(scroll_x=False)
        box = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        btn_rand_clr = wx.Button(panel, wx.ID_ANY, "Random Colors")
        btn_rand_clr.Bind(wx.EVT_BUTTON, globals.lightFunc)

        btn_turn_all_on = wx.Button(panel, wx.ID_ANY, "Turn All Lights On")
        btn_turn_all_on.Bind(wx.EVT_BUTTON, globals.allOn)

        btn_turn_all_off = wx.Button(panel, wx.ID_ANY, "Turn All Lights Off")
        btn_turn_all_off.Bind(wx.EVT_BUTTON, globals.allOff)


        for light_num,light in enumerate(globals.b.lights):
            print "light_num: "+str(type(light_num))
            print "light: "+str(light)
            light_label = wx.StaticText(panel, label=globals.b.get_light(light_num+1,'name')+": ")
            hslider = wx.Slider(panel, -1, globals.b.get_light(light_num+1,'bri'), 0, 254,
                size=(250, -1),
                style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
            hslider.SetTickFreq(5)
            hslider.Bind(wx.EVT_SCROLL, lambda event,light_id=(light_num+1): ui.scrollHandler(event,light_id))
            box.Add(light_label, 0, wx.ALL, 10)
            box.Add(hslider, 0, wx.ALL, 10)

        box.Add(btn_rand_clr, 0, wx.ALL, 10)
        box.Add(btn_turn_all_on, 0, wx.ALL, 10)
        box.Add(btn_turn_all_off, 0, wx.ALL, 10)

        hbox.Add(box, 0, wx.ALL, 10)

        panel.SetSizer(hbox)
        panel.Layout()
        self.Show()

    def OnClose(self,event):
        self._light_thread.stop()
        self.Destroy()
