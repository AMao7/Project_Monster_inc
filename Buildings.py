class Buildings():


    def __init__(self, location, capacity, people_in_building = 0):
        self.location = location
        self.capacity = capacity
        self.people_in_building = people_in_building

    def toggle_lights(self):
        if self.people_in_building > 1:
            return 'lights on'
        else:
            return 'lights off'


building_1 = Buildings('London', 500, people_in_building = 2)
building_2 = Buildings('London', 500, people_in_building = 0)
print(building_1.toggle_lights())
print(building_2.toggle_lights())