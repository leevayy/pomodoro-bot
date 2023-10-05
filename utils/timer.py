import time

def set_timeout(func,timer):
    time.sleep(timer)
    func()
