"""

:file: tornado-lightning-talk/src/app.py
:author: husobee
:date: 2014-08-01
:license: MIT License, 2014

Example tornado application, for OSS lightning talk

"""

from tornado import ioloop, web
from models import BlockyCrypto
import json

class HelloHandler(web.RequestHandler):

    def _blocky_crypto_process_callback(self, result):
        self.set_status(200) # set the response status when we get the result back
        self.write(json.dumps(dict(hello=result.result()))) #write the json in the response body
        self.finish() # finish the asynch call

    @web.asynchronous
    def get(self):
        try:
            BlockyCrypto().blocky_crypto_process("world", callback=self._blocky_crypto_process_callback) # call our new blocky crypto instance
        except Exception as e:
            self.set_status(500)
            self.write("An Exception has occurred: {0}".format(e))
            self.finish()

application = web.Application([ # here is our url/handler mappings, application url routing
    (r"/hello/", HelloHandler), # main handler takes a url parm, and we are passing session to initialize
])

if __name__ == "__main__": # main
    application.listen(8080) # listen on 8080
    ioloop.IOLoop.instance().start() # startup ioloop
