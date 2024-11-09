import turtle
import random

class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def move(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

class PolygonArt:
    def __init__(self):
        self.turtle_settings = {
            'speed': 0,
            'bgcolor': 'black',
            'colormode': 255,
            'tracer': 0
        }
        self.num_sides = random.randint(3, 5)
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618

    def run(self):
        turtle.speed(self.turtle_settings['speed'])
        turtle.bgcolor(self.turtle_settings['bgcolor'])
        turtle.tracer(self.turtle_settings['tracer'])
        turtle.colormode(self.turtle_settings['colormode'])

        polygon1 = Polygon(self.num_sides, self.size, self.orientation, self.location, self.color, self.border_size)
        polygon1.draw()

        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]

        self.size *= self.reduction_ratio
        polygon2 = Polygon(self.num_sides, self.size, self.orientation, self.location, self.color, self.border_size)
        polygon2.draw()

        turtle.done()

class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_levels, reduction_ratio):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.num_levels = num_levels
        self.reduction_ratio = reduction_ratio

    def draw(self):
        for level in range(self.num_levels):
            super().draw()
            self.size *= self.reduction_ratio
            self.location[0] += self.size * (1 - self.reduction_ratio) / 2
            self.location[1] += self.size * (1 - self.reduction_ratio) / 2

if __name__ == "__main__":
    app = PolygonArt()
    app.run()
