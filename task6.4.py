class Car:
    def __init__(self, speed, color, name, is_police):
        self.sp = speed
        self.col = color
        self.n = name
        self.isp = is_police

    def go(self):
        print("Go")

    def stop(self):
        print("Stop")

    def turn_right(self):
        print('Turn right')

    def turn_left(self):
        print("Turn left")

    def show_speed(self):
        print(self.sp)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.sp < 60:
            print(self.sp)
        else:
            print(self.sp, "Over speed!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.sp < 40:
            print(self.sp)
        else:
            print(self.sp, "Over speed!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


my_car = TownCar(60, "Green", "Ford", False)
print(my_car.n)
my_car.go()
my_car.turn_right()
my_car.show_speed()

police = PoliceCar(70, "Black", "Honda", True)
print(police.col)
police.show_speed()
print(police.isp)
