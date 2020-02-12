from Buildings import Buildings

class Classroom(Buildings):
    def __init__(self, location, capacity, lights):
        super().__init__(location, capacity, lights)