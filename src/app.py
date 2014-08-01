"""

:file: tornado-lightning-talk/src/app.py
:author: husobee
:date: 2014-08-01
:license: MIT License, 2014

Example tornado application, for OSS lightning talk

"""

from tornado import ioloop, web
from models import blocky_crypto_process
import json

class HelloHandler(web.RequestHandler):
    def get(self):
        result = None
        try:
            result = blocky_crypto_process("world")
        except Exception as e:
            self.set_status(500)
            self.write("An Exception has occurred: {0}".format(e))
        self.set_status(200)
        self.write(json.dumps(dict(hello=result)))

application = web.Application([ # here is our url/handler mappings, application url routing
    (r"/hello/", HelloHandler), # main handler takes a url parm, and we are passing session to initialize
])

if __name__ == "__main__": # main
    application.listen(8080) # listen on 8080
    ioloop.IOLoop.instance().start() # startup ioloop
