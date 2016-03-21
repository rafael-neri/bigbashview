#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import globals as globaldata
#from bbv.server.bbv2server import run_server
from utils import *


class Bigbashview:

    width = globaldata.WIDTH
    height = globaldata.HEIGHT
    url = globaldata.URL
    window_state = globaldata.WINDOW_STATE
    icon = globaldata.ICON

    def init(self):

        # Get And Verify Options And Arguments
        try:
            options, arguments = Utils.getOptionsAndArgs(sys.argv[1:])
            Utils.parseOptions(options)
            if not arguments:
                raise Exception()
        except:
            Utils.help()

        # Set URL
        self.url = arguments[0]

        # Execute Options
        for option, value in options:
            if option in ('-h', '--help'):
                Utils.help()
            elif option in ('-v', '--version'):
                print(globaldata.APP_NAME, globaldata.APP_VERSION)
                sys.exit()
            elif option in ('-s', '--screen'):
                screen = value.split('x')
                self.width, self.height = screen
                self.width = int(self.width)
                self.height = int(self.height)
            elif option in ('-w', '--window_state'):
                    self.window_state = value
            elif option in ('-i', '--icon'):
                self.icon = value

        # Create data folder if doesn't exists...
        if not os.path.isdir(globaldata.DATA_DIR):
            os.mkdir(globaldata.DATA_DIR)

        # Construct Window
        try:
            import qt5
        except ImportError:
            print('Bigbashview needs PyQt5 to run.')
            print('Please install the latest stable version')
            sys.exit(1)
        self.window = qt5.Window()

    def execute(self, server=True):
        #if server:
            #run_server()

        self.window.set_size(self.width, self.height)
        self.window.show(self.window_state)

        if self.url.find('://') == -1:
            if not self.url.startswith('/'):
                self.url = '/' + self.url
            self.url = "http://%s:%s%s" % (globaldata.ADDRESS(), globaldata.PORT(), self.url)

        self.window.load_url(self.url)
        sys.exit(self.window.run())

