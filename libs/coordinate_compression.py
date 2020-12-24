"""
Coordinate compression (CoCo) / Zahyo Asshuku
"""


class CoordinateCompression:
    def __init__(self):
        self.values = []

    def add(self, x):
        self.values.append(x)

    def compress(self):
        self.values.sort()
        x2i = {}
        for i, x in enumerate(self.values):
            x2i[x] = i
        self.x2i = x2i
        self.i2x = self.values
        return self.x2i, self.i2x
