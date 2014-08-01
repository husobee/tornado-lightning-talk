"""

:file: tornado-lightning-talk/src/models.py
:author: husobee
:date: 2014-08-01
:license: MIT License, 2014

Example tornado application, for OSS lightning talk.

Models are data access models

"""

import time

def blocky_crypto_process(plaintext):
    time.sleep(15)
    ciphertext = plaintext
    return ciphertext
