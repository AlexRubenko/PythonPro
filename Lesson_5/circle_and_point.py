import math
import numpy as np
import matplotlib.pyplot as plt


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def plot_graph(self, point):
        theta = np.linspace(0, 2*np.pi, 100)
        #  Here we use the parametric equation of the circle
        x = self.x + self.radius * np.cos(theta)
        y = self.y + self.radius * np.sin(theta)

        plt.plot(x, y)
        plt.scatter(self.x, self.y, color='blue', label='Centr')
        plt.scatter(point.x, point.y, color='red', label='Centre')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.gca().set_aspect('equal')  # Set equal aspect ratio
        plt.grid(True)
        plt.show()

    def contains(self, point):
        #  And then I decided to use the canonical equation of the circle
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        if distance <= self.radius:
            self.plot_graph(point)
            return True
        else:
            self.plot_graph(point)
            return False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    circle = Circle(0, 0, 5)
    point1 = Point(1, 2)
    print(circle.contains(point1))


if __name__ == "__main__":
    main()
