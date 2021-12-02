class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name}  started'

    def stop(self):
        return f'{self.name}  stopped'

    def turn_right(self):
        return f'{self.name} turned right'

    def turn_left(self):
        return f'{self.name} turned left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed} mph'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allowed for town car'
        else:
            return f'Speed of {self.name} is ok for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allowed for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


audi = SportCar(100, 'Red', 'Audi', False)
shkoda = TownCar(30, 'White', 'Shkoda', False)
bmw = WorkCar(70, 'Rose', 'BMW', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(shkoda.turn_left())
print(f'When {shkoda.turn_right()}, then {audi.stop()}')
print(f'{bmw.go()} with speed exactly {bmw.show_speed()}')
print(f'{bmw.name} is {bmw.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {bmw.name}  a police car? {bmw.is_police}')
print(audi.show_speed())
print(shkoda.show_speed())
print(ford.police())
print(ford.show_speed())

