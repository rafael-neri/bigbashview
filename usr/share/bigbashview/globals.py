#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

# Application
APP_NAME = "BigBashView"
APP_VERSION = "3.0.0"

# Directories
PROGDIR = os.path.dirname(os.path.abspath(sys.argv[0]))
DATA_DIR = os.path.expanduser("~/.bigbashview")

# Server
ADDRESS = "127.0.0.1"
PORT = 6543
COMPAT = True

# Window
WIDTH = -1
HEIGHT = -1
WINDOW_STATE = "normal"
URL = "/"

# Extras
ICON = os.sep.join((PROGDIR, "images", "icone.png"))