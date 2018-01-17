class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("Hello World")


m = Man("David")
m.hello()
Man.hello(m)