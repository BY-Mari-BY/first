import time

class TrafficLights:
    _color = None
    _colors = ['red', 'yellow', 'green']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i = 0
        while i<5:
            for el in TrafficLights._colors:
                print(el)
                i +=1
                time.sleep(1)
traffic = TrafficLights()
traffic.running()



