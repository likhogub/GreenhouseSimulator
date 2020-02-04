import math
from matplotlib import pyplot as plt

class Temp():
    import random

    def __init__(self):
        self.temp = 25

    def change(self):
        self.temp += self.random.choice((-1, 1))*0.1
        if self.temp > 45:
            self.temp = 45
        elif self.temp < 15:
            self.temp = 15

    def get(self):
        return self.temp


class Hum():
    import random
    import math
    def __init__(self):
        self.hum = 50

    def decrease(self, temp):
        self.hum -= 0.1 * self.math.sqrt((temp + 25) / 75) * self.math.sqrt(self.random.random())
        if self.hum < 1:
            self.hum = 1

    def water(self):
        self.hum += 0.5

    def get(self):
        return self.hum


class Greenhouse():
    from matplotlib import pyplot as plt

    def __init__(self):
        self.temp = Temp()
        self.hum = Hum()
        self.watering = False
        self.time = 0
        self.last = 50
        self.temps = []
        self.hums = []
        self.waterings = []

    def start(self):
        self.plt.ion()
        fig, ax = self.plt.subplots()
        while True:
            self.time += 1
            if (self.hum.get() < 25) and (self.temp.get() > 25):
                self.watering = True
            elif self.hum.get() > 75:
                self.watering = False
            if self.watering:
                self.hum.water()
            self.temp.change()
            self.hum.decrease(self.temp.get())
            self.temps.append(self.temp.get())
            self.hums.append(self.hum.get())
            self.waterings.append(int(self.watering))
            self.plt.clf()
            self.plt.subplot(2, 1, 1)
            self.plt.plot(self.temps[-500::10])
            self.plt.subplot(2, 1, 2)
            self.plt.plot(self.hums[-500::10])
            self.plt.draw()
            self.plt.pause(0.001)

