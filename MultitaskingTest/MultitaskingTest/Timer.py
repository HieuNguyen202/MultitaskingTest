import time
class Timer:
    def __init__(self):
        self._timer=time.time()

    def reset(self):
	    self._timer = time.time()

    def getTime(self):
	    return time.time()-self._timer

