# -*- coding: utf-8 -*-

import os
import json
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.web

from Lib.dict_objectified import DictObject

def launch(host, port, route):
    with open(os.path.dirname(__file__) + '/service.config') as file:
        svr = DictObject(json.loads(file.read()))
    for i in svr.route:
        for j in i.values():
            pyfile = j.keys()[0]
            pyfunc = j[j.keys()[0]]
            impstring = "from handler.{pyfile} import {handler}".format(pyfile=pyfile, handler=pyfunc)
            exec impstring
    print svr.route
    print [(route + i.keys()[0], i.values()[0].values()[0]) for i in svr.route]
    app = tornado.web.Application(
        handlers=[(route + i.keys()[0], i.values()[0].values()[0]) for i in svr.route],
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
