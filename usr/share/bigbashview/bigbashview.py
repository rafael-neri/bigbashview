#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import getopt

import globals as globaldata
#from bbv.server.bbv2server import run_server


# TODO: Implement Translations


class Bigbashview:

    width = -1
    height = -1
    toolkit = "qt4"
    url = "/"
    window_state="normal"
    icon = globaldata.ICON

    def __init__(self):
        try:
            options, arguments = getopt.gnu_getopt(
                sys.argv[1:],
                'hs:vw:i:c',
                ['help', 'screen=', 'version', 'window_state=', 'icon=', 'compatibility-mode' ]
            )
        except(getopt.error):
            print('for help use --help')
            sys.exit(2)

        if len(arguments):
            self.url=arguments[0]

    #    for o, a in options:
    #        if o in ('-h', '--help'):
    #            self.help()

    #        elif o in ('-v','--version'):
    #            print globaldata.APP_NAME, globaldata.APP_VERSION
    #            sys.exit()

    #        elif o in ('-s', '--screen'):
    #            args = a.split('x')

    #            if len(args) != 2:
    #                self.help()

    #            for i in args:
    #                if not i.isdigit():
    #                    self.help()

    #            self.width, self.height = args

                #Window Size
    #            self.width = int(self.width)
    #            self.height = int(self.height)

    #        elif o in ('-t','--toolkit'):
    #            if a in ("gtk2", "qt4"):
    #                self.toolkit = a
    #            else:
    #                self.toolkit = "auto"
    #        elif o in ('-w','--window_state'):
    #            if a in ("normal","maximized","fullscreen"):
    #                self.window_state=a
    #        elif o in ('-i','--icon'):
    #            if os.path.exists(a):
    #                globaldata.ICON = a
    #        elif o in ('-c','--compatibility-mode'):
    #                globaldata.COMPAT = True

        #Create data folder if doesn't exists...
    #    if not os.path.isdir(globaldata.DATA_DIR):
    #        os.mkdir(globaldata.DATA_DIR)

        #construct window
    #    if self.toolkit == "auto":
    #        try:
    #            from bbv.ui import qt4
    #            has_qt4 = True
    #        except ImportError:
    #            has_qt4 = False

    #        try:
    #            from bbv.ui import gtk2
    #            has_gtk2 = True
    #        except ImportError:
    #            has_gtk2 = False

    #        if not(has_qt4) and not(has_gtk2):
    #            print >> sys.stderr, ('bbv needs PyGTK or PyQt '
    #                                  'to run. Please install '
    #                                  'the latest stable version')
    #            sys.exit(1)

    #        elif has_qt4:
    #            self.window = qt4.Window()
    #        elif has_gtk2:
    #            self.window = gtk2.Window()

    #    elif self.toolkit == "qt4":
    #        try:
    #            from bbv.ui import qt4
    #            has_qt4 = True
    #        except ImportError:
    #            has_qt4 = False

    #        if not has_qt4:
    #            from bbv.ui import qt4
    #            print >> sys.stderr, ('bbv needs PyQt '
    #                                  'to run. Please install '
    #                                  'the latest stable version')

    #            sys.exit(1)

    #        self.window = qt4.Window()

    #    elif self.toolkit == "gtk2":
    #        try:
    #            from bbv.ui import gtk2
    #            has_gtk2 = True
    #        except ImportError:
    #            has_gtk2 = False

    #        if not has_gtk2:
    #            print >> sys.stderr, ('bbv needs PyGTK '
    #                                  'to run. Please install '
    #                                  'the latest stable version')

    #            sys.exit(1)

    #        self.window = gtk2.Window()


    #def help(self):
    #    print sys.argv[0], '[-h|--help] [-s|--screen=widthxheight] [-v|--version] [-t|--toolkit=[gtk2|qt4|]] [-w|--window_state=[normal|maximized|fullscreen]] [-i|--icon image] [-c|--compatibility-mode] URL'
    #    sys.exit()

    def execute(self, server=True):
        pass
        #if server:
        #    run_server()
        #self.window.set_size(self.width,self.height)
        #self.window.show(self.window_state)
        #if self.url.find('://') == -1:
        #    if not self.url.startswith('/'):
        #        self.url = '/'+self.url
        #    self.url = "http://%s:%s%s" %(globaldata.ADDRESS(),globaldata.PORT(),self.url)
        #self.window.load_url(self.url)
        #globaldata.ICON = self.icon
        #sys.exit(self.window.run())
