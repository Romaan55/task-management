import threading
import time
def debounce(fn, delay):
    timer = None
    def wrapper(*args):
        nonlocal timer
        if timer is not None: #Agar pehle se timer chal raha hai, usko cancel karo
            timer.cancel()

        timer = threading.Timer(delay, fn, args=args)#New timer start kara ga
        timer.start()

    def cancel():
        nonlocal timer
        if timer is not None:
            timer.cancel()
            timer = None

    wrapper.cancel = cancel
    return wrapper

def hello(name): #Normal function
    print("Hello", name)

debounced_hello = debounce(hello, 2) #Debounced function
debounced_hello("Ali")  #Multiple calls
time.sleep(0.5)

debounced_hello("Ahmed")
time.sleep(0.5)

debounced_hello("Romaan")
time.sleep(3)  #2 seconds wait