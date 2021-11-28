#3.	Напишите  функцию типа "фабрика объектов" и используйте ее для создания в цикле объектов разных типов.
# После создания объекта определите его реальный тип и выполните с ним  действия.
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def Create_Student(self) -> CreaterStudent:
        pass

    @abstractmethod
    def Create_Extramural(self) -> CreaterExtramural:
        pass


class ConcreteFactory1(AbstractFactory):
    def Create_Student(self) -> CreaterStudent:
        return StudentProduct1()

    def Create_Extramural(self) -> CreaterExtramural:
        return ExtramuralProduct1()


class ConcreteFactory2(AbstractFactory):
    def Create_Student(self) -> CreaterStudent:
        return StudentProduct2()

    def Create_Extramural(self) -> CreaterExtramural:
        return ExtramuralProduct2()


class CreaterStudent(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class StudentProduct1(CreaterStudent):
    def useful_function_a(self) -> str:
        return "The result of the product Student1."
class StudentProduct2(CreaterStudent):
    def useful_function_a(self) -> str:
        return "The result of the product Student2."


class CreaterExtramural(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: CreaterStudent) -> None:
        pass

class ExtramuralProduct1(CreaterExtramural):
    def useful_function_b(self) -> str:
        return "The result of the product Extramural1."
    def another_useful_function_b(self, collaborator: CreaterStudent) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the Extramural1 collaborating with the ({result})"


class ExtramuralProduct2(CreaterExtramural):
    def useful_function_b(self) -> str:
        return "The result of the product Extramural2."
    def another_useful_function_b(self, collaborator: CreaterStudent):
        result = collaborator.useful_function_a()
        return f"The result of the Extramural2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    k=0
    while k>=0:
        x=int(input())
        if x==1:
            product_a = factory.Create_Student()
            print(f"{product_a.useful_function_a}")
        elif x==2:
            product_b = factory.Create_Extramural()
            print(f"{product_b.useful_function_b()}")

client_code(ConcreteFactory1())
client_code(ConcreteFactory2())

