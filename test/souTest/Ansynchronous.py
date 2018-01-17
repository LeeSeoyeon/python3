from queue import Queue
from functools import partial

eventloop = None

class EventLoop(Queue):
    def start(self):
        while True:
            function = self.get()
            function()


def sayHello():
    global eventloop
    print("hello")
    eventloop.put(sayWorld)

def sayWorld():
    global eventloop
    print("world")
    eventloop.put(sayHello)

if __name__ == "__main__":
    eventloop = EventLoop()
    eventloop.put(sayHello)
    eventloop.start()

