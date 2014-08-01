"""

:file: tornado-lightning-talk/src/models.py
:author: husobee
:date: 2014-08-01
:license: MIT License, 2014

Example tornado application, for OSS lightning talk.

Models are data access models

"""

import time
from tornado import ioloop # get the io loop
from tornado.concurrent import return_future, run_on_executor # helpers 
from concurrent.futures import ThreadPoolExecutor # a threadpool executor


EXECUTOR = ThreadPoolExecutor(2) # this will make an executor pool of 1 thread

class BlockyCrypto(object): 
    """ In order to use tornado.concurrent decorators, we need to have class attributes executor and io_loop"""
    executor = EXECUTOR # this is our module level executor
    io_loop = ioloop.IOLoop.instance() #this is our io_loop snagged from tornado

    @run_on_executor #this method will be run on the executor
    @return_future # and it will return a future
    def blocky_crypto_process(self, plaintext, callback=None):
        time.sleep(10)
        ciphertext = plaintext
        callback(ciphertext)
