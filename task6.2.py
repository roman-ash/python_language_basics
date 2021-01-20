class Road:
    def __init__(self, length, width):
        self._le = length
        self._wi = width

    def total_mass_of_asphalt(self):
        print(self._le * self._wi * 125)


road_1 = Road(20, 5000)
road_1.total_mass_of_asphalt()
