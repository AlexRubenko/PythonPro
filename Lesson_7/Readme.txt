2. Створити frange ітератор. Який буде працювати з float.

class frange:
    pass

for i in frange(1, 100, 3.5):
    print(i)

має вивести

1
4.5
8.0
...


Перед здачею перевірти тести чи проходять:

assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')

3. Створити context manager який буде фарбувати колір виведеного тексту

https://www.skillsugar.com/how-to-print-coloured-text-in-python

Приклад:

print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with colorizer('red'):
    print('printed in red')
print('printed in default color')


4. Реалізувати метод square в фігурах які залишилися. (Triangle+Parallelogram).

Triangle - треба створити клас

class Shape: #class Shape(object)    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def square(self):
        return 0
    
    
class Circle(Shape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        
    def square(self):
        return math.pi*self.radius**2
    
    
class Rectangle(Shape):
    
    def __init__(self, x, y, height, width):
        super().__init__(x, y) 
        self.height = height
        self.width = width


    def square(self):
        return self.width*self.height
    
    
class Parallelogram(Rectangle):


    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width) 
        self.angle = angle


    def print_angle(self):
        print(self.angle)
        
    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


    
class Scene:
    def __init__(self):
        self._figures = []
        
    def add_figure(self, figure):
        self._figures.append(figure)
     
    def total_square(self):
        return sum(f.square() for f in self._figures)
    
    def __str__(self):
        pass
        
r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)


c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)


p = Parallelogram(1, 2, 20, 30, 45)
p.x
p1 = Parallelogram(1, 2, 20, 30, 45)
str(p1)


scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)


scene.total_square()

