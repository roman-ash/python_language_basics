class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.sn = surname
        self.pos = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.n, self.sn)

    def get_total_income(self):
        print(self._income["wage"] + self._income["bonus"])


a = Position("Max", "Mad", "Driver", 1500, 500)
print(a.pos)
a.get_full_name()
a.get_total_income()
