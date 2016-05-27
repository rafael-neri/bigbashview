#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from server import *
from utils import *
import globals as globaldata
import qt5


class Bigbashview:

    width = globaldata.WIDTH
    height = globaldata.HEIGHT
    url = globaldata.URL
    window_state = globaldata.WINDOW_STATE
    icon = globaldata.ICON

    def __init__(self):

        # Get And Verify Options And Arguments
        try:
            options, arguments = utils.get_options_and_args(sys.argv[1:])
            utils.parse_options(options)
        except:
            utils.help()

        # Set URL
        if arguments:
            self.url = arguments[0]

        # Execute Options
        for option, value in options:
            if option in ('-h', '--help'):
                utils.help()
            elif option in ('-v', '--version'):
                utils.version()
            elif option in ('-s', '--screen'):
                screen = value.split('x')
                self.width, self.height = screen
                self.width = int(self.width)
                self.height = int(self.height)
            elif option in ('-w', '--window_state'):
                    self.window_state = value
            elif option in ('-i', '--icon'):
                self.icon = value

        # check if url is empty
        if not self.url:
            utils.help()

        # Create data folder if doesn't exists...
        if not os.path.isdir(globaldata.DATA_DIR):
            os.mkdir(globaldata.DATA_DIR)

        # Construct Window
        self.window = qt5.Window()

    def execute(self, server=True):
        if server:
            run_server()

        self.window.set_size(self.width, self.height)
        self.window.show(self.window_state)

        if self.url.find('://') == -1:
            if not self.url.startswith('/'):
                self.url = '/' + self.url
            self.url = "http://%s:%s%s" % (globaldata.ADDRESS, globaldata.PORT, self.url)

        print((type(self.url)))
        #sys.exit()

        self.window.load_url(self.url)
        sys.exit(self.window.run())

