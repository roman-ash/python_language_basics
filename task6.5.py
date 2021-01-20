class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print(f"Запуск отрисовки ({self.t}).")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки ручкой {self.t}.")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки карандашом {self.t}.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки маркером {self.t}.")


my_pen = Pen("Bic")
my_pen.draw()
my_stationery = Stationery("ErichKrause")
my_stationery.draw()
