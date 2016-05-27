#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import web
import sys
import socket
import threading
# import views
import globals as globaldata


class Server(threading.Thread):
    def _get_subclasses(self, classes=None):
        """ Get subclasses recursively """
        if classes is None:
            classes = views.url_handler.__subclasses__()
        result = classes
        for cls in classes:
            result += self._get_subclasses(cls.__subclasses__())
        return result

    def get_urls(self):
        """ Return supported URLs. """
        classes = self._get_subclasses()
        result = []
        for cls in classes:
            result.append(cls.__url__)
            result.append(cls.__name__)
        return tuple(result)

    def get_classes(self):
        """ Return all view classes. """
        classes = self._get_subclasses()
        result = {}
        for cls in classes:
            result[cls.__name__] = cls
        return result

    def run(self):
        """ Run the webserver """
        ip = globaldata.ADDRESS()
        port = globaldata.PORT()
        sys.argv = [sys.argv[0], '']
        sys.argv[1] = ':'.join((ip, str(port)))

        urls = self.get_urls()
        classes = self.get_classes()
        app = web.application(urls, classes)
        app.run()

    def stop(self):
        pass


def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


def run_server(ip='127.0.0.1', background=True):
    port = get_open_port()
    globaldata.ADDRESS = lambda: ip
    globaldata.PORT = lambda: port

    server = Server()

    if background:
        server.daemon = True
        web.config.debug = False
        server.start()
    else:
        web.config.debug = True
        server.run()


if __name__ == "__main__":
    run_server(background=False)
