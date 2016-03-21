#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QObject, pyqtSignal, QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWebKit import QWebSettings
from globals import ICON, DATA_DIR

class Window():

    def __init__(self):
        self.debug = 1
        self.app = QApplication([])
        self.desktop = QApplication.desktop()
        self.web = QWebView()
        self.icon = QIcon(ICON)
        QWebSettings.setIconDatabasePath(DATA_DIR)
        #self.web.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)

        # Signals
        #self.connect(self.web, pyqtSignal("titleChanged ( const QString &)"), self.title_changed)
        #self.connect(self.web, pyqtSignal("iconChanged ()"), self.icon_changed)
        #self.connect(self.web.page(), pyqtSignal("windowCloseRequested ()"), self.close_window)
        #self.connect(self.web.page(), pyqtSignal("geometryChangeRequested ( const QRect)"), self.set_geometry)

    def handle_trigger(self):
        # Show that the slot has been called.
        print("trigger signal received")

    def show(self, window_state):
        if window_state == "maximized" and not self.web.isMaximized():
            self.web.showMaximized()
        elif window_state == "fullscreen" and not self.web.isFullScreen():
            self.web.showFullScreen()
        elif window_state == "normal":
            self.web.showNormal()
        else:
            self.web.show()

    def run(self):
        return self.app.exec_()

    def set_debug(self, debuglevel):
        self.debug = debuglevel

    def set_geometry(self, geom):
        self.web.setGeometry(geom)

    def close_window(self):
        sys.exit()

    def icon_changed(self):
        if not self.icon.isNull():
            self.web.setWindowIcon(self.icon)
        if not self.web.icon().isNull():
            self.web.setWindowIcon(self.web.icon())

    def title_changed(self, title):
        self.web.setWindowTitle(title)

    def load_url(self, url):
        self.url = QUrl.fromEncoded(url)
        self.web.setUrl(self.url)

    def set_size(self, width, height):
        if width <= 0:
            width = 640
        if height <= 0:
            height = 480
        left = (self.desktop.width() - width) / 2
        top = (self.desktop.height() - height) / 2
        self.web.setGeometry(left, top, width, height)