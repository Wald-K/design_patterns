"""Umożliwia tworzenie w runtimie obiektu uzależnionego
od parametru person_type
"""
from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def get_info(self):
        """Interface method"""


class Student(IPerson):
    def __init__(self, name):
        self.name = name

    def get_info(self):
        print(f"Im Student called {self.name}")


class Teacher(IPerson):
    def __init__(self, name):
        self.name = name

    def get_info(self):
        print(f"Im Teacher called {self.name}")


class PersonFactory:
    @staticmethod
    def create_person(person_type: str, name: str) -> IPerson:
        if person_type == "Student":
            return Student(name)
        if person_type == "Teacher":
            return Teacher(name)
        else:
            raise NotImplementedError


s = PersonFactory.create_person("Student", "Wald")
t = PersonFactory.create_person("Teacher", "Tom")
z = PersonFactory.create_person()

s.get_info()
t.get_info()
