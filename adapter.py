class Adaptee:

    def methodA(self):
        print("Called methodA from Adaptee")


class Adapter:

    def __init__(self):
        self.__adaptee = Adaptee()

    def methodB(self):
        self.__adaptee.methodA()


if __name__ == "__main__":
    adapter = Adapter()

    adapter.methodB()
