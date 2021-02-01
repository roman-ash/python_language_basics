from abc import ABC, abstractmethod


class OfficeEquipmentWarehouse:
    def __init__(self, name, price_for_one, quantity):
        self.name = name
        self.pfo = price_for_one
        self.qua = quantity

    def __str__(self):
        if type(self.name) == str and type(self.pfo) == int and type(self.qua) == int:
            return f"name: {self.name}\nprice for one: {self.pfo}\nquantity: {self.qua}"
        else:
            return "Invalid data."


class OfficeEquipment(ABC):
    @abstractmethod
    def copy(self):
        pass


class Printer(OfficeEquipment, OfficeEquipmentWarehouse):
    def copy(self):
        print(f"{self.name}. Transfer of information from electronic format to paper.")


class Scanner(OfficeEquipment, OfficeEquipmentWarehouse):
    def copy(self):
        print(f"{self.name}. Transfer of information from paper to electronic format.")


e1 = Printer("HP", 200, 4)
print(e1)
e1.copy()
e2 = Scanner("Fony", 100, "two")
print(e2)
