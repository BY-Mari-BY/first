class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Start drawing')
class Pen(Stationery):
    def draw(self):
        print('Drawing by pen')
class Pencil(Stationery):
    def draw(self):
        print('Drawing by pencil')
class Handle(Stationery):
    def draw(self):
        print('Drawing by marker')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()

