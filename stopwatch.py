import time

class stopwatch :
    def __init__(self):
        self.c = time.time()

    def ellapsed(self):
        return time.time() - self.c

    def pause(self):
        self.c = time.time() - self.c

    def resume(self):
        self.c = time.time() - self.c

    def reset(self):
        self.c = time.time()

    def ratio(self,milis):
        return milis / self.ellapsed()