#!/usr/bin/python

import wx
import ui
import globals
from phue import Bridge
from phue import PhueRegistrationException as BridgeButtonException
from phue import PhueRequestTimeout
from socket import error as SocketError
from socket import timeout
from frame import Frame
import time
import sys
import signal
from threading import Thread
import threading
import logging
import lights




if __name__=='__main__':
    try:
        globals.init()
        globals.light_thread = lights.LightThread(globals.lightFunc)
        logging.basicConfig()
        app=wx.App(False)
        try:
            import config
            bridge_ip = config.bridge['ip']
        except ImportError:
            bridge_ip = ui.ask(message='What is your bridge IP address?')
            file = open('config.py','w')
            file.write('bridge={\'ip\':\''+bridge_ip+'\'}')
            file.close()
        if bridge_ip:
            print(u"Bridge IP is: "+bridge_ip)
            try:
                globals.b = Bridge(bridge_ip)
                globals.lights = globals.b.get_light_objects('id')
                frame=Frame(globals.light_thread)
                frame.Maximize()
                app.MainLoop()
            except BridgeButtonException:
                print("Button on bridge needs to be pressed within 30 seconds. Please try again.")
                globals.light_thread.stop()
                sys.exit(0)
            except (SocketError, PhueRequestTimeout) as e:
                print("Could not connect to bridge: "+str(e))
                globals.light_thread.stop()
                sys.exit(0)
        else:
            print("Quitting...")
            globals.light_thread.stop()
            sys.exit(0)
    except KeyboardInterrupt:
        globals.light_thread.stop()
        sys.exit(0)
