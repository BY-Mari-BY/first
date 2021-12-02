class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('To construct a road its needed')

    def intake(self):
        self.weigth = 25
        self.thickness = 0.05
        intake = self.length * self.width * self.weigth * self.thickness / 1000
        print(f' {intake} tons of asphalt')

road = Road(20000, 6)
road.intake()

