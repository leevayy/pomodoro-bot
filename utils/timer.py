import time

def set_timer(func,timer):
    time.sleep(timer)
    func()
    