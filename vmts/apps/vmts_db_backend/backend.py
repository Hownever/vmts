# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.web
import tornado.ioloop

try:
    from vmts_pre_define import cfg
    from vmts_logger import VmtsLogger
except ImportError:
    raise ImportError('Vmts environment had not be initialized.')

from urls import urls

config = cfg.get_module('vmts_apps')


def run():
    """
    vmts database backend entrance function.
    :return: None
    """

    settings = config.backend.settings
    app = tornado.web.Application(
        handlers=urls,
        debug=config.backend.debug,
        **settings
    )

    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(config.backend.port)
    tornado.ioloop.IOLoop.instance().start()
    VmtsLogger('info').info('Vmts database backend started.')

if __name__ == "__main__":
    run()