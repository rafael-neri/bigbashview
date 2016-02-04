#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

APP_NAME = "BigBashView"
APP_VERSION = "3.0.0"
PROGDIR=os.path.dirname(os.path.abspath(sys.argv[0]))

if os.path.isdir(os.sep.join((PROGDIR,".hg"))):
    try:
        import subprocess
        po = subprocess.Popen("hg heads --template '{rev}'", stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = po.communicate()
        APP_VERSION+=' (DEV. VERSION) rev %s' %stdout
    except:
        pass

DATA_DIR = os.path.expanduser("~/.bigbashview") # TODO: Check portability issues
ICON = os.sep.join((PROGDIR,"bbv","img","icone.png"))
ADDRESS = lambda: '127.0.0.1'
PORT = lambda: 9000
COMPAT=False
