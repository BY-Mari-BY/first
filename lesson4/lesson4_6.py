from itertools import cycle, count
n = 100
list = [i+3 for i in range(8)]
counter = count()
cycler = cycle(list)
print([next(counter) for i in range(n)])
print([next(cycler) for i in range(n)])



