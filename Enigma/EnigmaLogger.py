from __future__ import print_function

class EnigmaLogger():
    def __init__(self, verbose):
        self._verbose = verbose

    def Log(self, message):
        if self._verbose == True:
            print(message)


