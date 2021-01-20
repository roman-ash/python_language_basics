from time import sleep
from termcolor import cprint


class TrafficLight:
    __color = ["red", "yellow", "green"]

    def running(self):
        c = 0
        while c < 3:
            for i in TrafficLight.__color:
                if i == "red":
                    cprint(i, i)
                    sleep(7)
                elif i == "yellow":
                    cprint(i, i)
                    sleep(2)
                elif i == "green":
                    cprint(i, i)
                    sleep(5)
            c += 1


a = TrafficLight()
a.running()
