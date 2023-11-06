class Figure():
    def __init__(self, h, f):
        self.height = h
        self.fundament = f


class Qadrant(Figure):
    def info(self):
        return 'This figure is a quadrant'
    def square(self):
        if self.height == self.fundament and self.height > 0:
            return self.height**2
        else:
            return 'Еhere is no square with these sides'


class Rectangle(Figure):
    def info(self):
        return 'This figure is a rectangle'
    def square(self):
        if self.height and self.fundament > 0:
            return self.height*self.fundament
        else:
            return 'Еhere is no rectangle with these sides'


class Triangle(Figure):
    def info(self):
        return 'This figure is a triangle'
    def square(self):
        if self.height and self.fundament > 0:
            return self.height*self.fundament*0.5
        else:
            return 'Еhere is no triangle with these sides'


F1 = Triangle(3, 6)

print(F1.info())
print(F1.square())
