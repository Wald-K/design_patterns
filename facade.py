class Element1:

    def metoda(self):
        print("Metoda klasy Element1")


class Element2:

    def metoda(self):
        print("Metoda klasy Element2")


class Element3:

    def metoda(self):
        print("Metoda klasy Element3")


class Facade:

    def __init__(self):
        self.element = []
        self.element.append(Element1())
        self.element.append(Element2())
        self.element.append(Element3())


if __name__ == "__main__":
    api = Facade()
    api.element[0].metoda()
    api.element[1].metoda()
    api.element[2].metoda()
