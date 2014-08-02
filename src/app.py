"""

:file: tornado-lightning-talk/src/app.py
:author: husobee
:date: 2014-08-01
:license: MIT License, 2014

Example tornado application, for OSS lightning talk

"""

from tornado import ioloop, web, gen
from models import BlockyCrypto
import json

class HelloHandler(web.RequestHandler):
    @web.asynchronous # this is an async call
    @gen.coroutine # decorate this call as a coroutine for tornado
    def get(self):
        result = None
        try:
            result = yield gen.Task( # create a coroutine task
                BlockyCrypto().blocky_crypto_process,# that runs this method
                "world") # with this parameter
        except Exception as e:
            self.set_status(500)
            self.write("An Exception has occurred: {0}".format(e))
            self.finish()
        self.set_status(200) # set the response status when we get the result back
        self.write(json.dumps(dict(hello=result.result()))) #write the json in the response body
        self.finish() # finish the asynch call

application = web.Application([ # here is our url/handler mappings, application url routing
    (r"/hello/", HelloHandler), # main handler takes a url parm, and we are passing session to initialize
])

if __name__ == "__main__": # main
    application.listen(8080) # listen on 8080
    ioloop.IOLoop.instance().start() # startup ioloop
