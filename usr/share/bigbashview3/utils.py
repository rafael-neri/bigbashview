#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import getopt
import globals as globaldata


class utils:

    @staticmethod
    def get_options_and_args(argv):
        try:
            options, arguments = getopt.gnu_getopt(
                argv,
                'hs:vw:i:',
                ['help', 'screen=', 'version', 'window_state=', 'icon=']
            )
            return options, arguments
        except:
            raise Exception()

    @staticmethod
    def parse_options(options):
        long_options = ["--help", "--version", "--screen", "--window_state", "--icon"]
        short_options = ["-h", "-v", "-s", "-w", "-i"]

        for option, value in options:

            if not option in long_options and not option in short_options:
                raise Exception()

            if option in ('-s', '--screen'):
                screen = value.split('x')
                if len(screen) != 2 or (not screen[0].isdigit or not screen[1].isdigit()):
                    raise Exception()

                if option in ('-w', '--window_state'):
                    if not value in ("normal", "maximized", "fullscreen"):
                        raise Exception()

                if option in ('-i', '--icon'):
                    if not os.path.exists(value):
                        raise Exception()

    @staticmethod
    def help():
        print('Usage:')
        print('    bigbashview3 [OPTIONS] [FILE|URL]')
        print('')
        print('Options:')
        print('    -h, --help                                             Show help info.')
        print('    -i, --icon image                                       Set icon image')
        print('    -s, --screen=widthxheight                              Set dimensions of the window.')
        print('    -v, --version                                          Show number version.')
        print('    -w, --window_state=[normal|maximized|fullscreen]       Set Window state.')
        sys.exit()

    @staticmethod
    def version():
        print(globaldata.APP_NAME, globaldata.APP_VERSION)
        sys.exit()


