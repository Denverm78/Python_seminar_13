# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со 
# сторонами отрицательной длины.

class RectangleException(Exception):
    pass


class SideNumberException(RectangleException):
    def __init__(self, a_n, b_n):
        self.a_n = a_n
        self.b_n = b_n

    def __str__(self):
        return f'Длины сторон прямоугольника должны быть положительными и неравными нулю.\n' \
        f'А у вас "a" = {self.a_n}, "b" = {self.b_n}'

class SideCharException(RectangleException):
    def __init__(self, a_c, b_c):
        self.a_c = a_c
        self.b_c = b_c

    def __str__(self):
        return f'Длины сторон прямоугольника должны принимать только числовые значения.\n' \
        f'А у вас "a" = {self.a_c}, "b" = {self.b_c}'

class Rectangle:
    """The class contains a description of the rectangle and various operations with it"""
    def __init__(self, a, b=None):
        if b == None:
            b = a
        try:
            a = float(a)
            b = float(b)
        except:
            raise SideCharException(a, b)
        if a <= 0 or b <= 0:
            raise SideNumberException(a, b)
        if a < b:
            a, b = b, a    
        self.a = a
        self.b = b

    def perimeter(self):
        """Calculating the perimeter of a rectangle"""
        return (self.a + self.b) * 2

    def sq(self):
        """Calculating the area of a rectangle"""
        return self.a * self.b
    
    def __add__(self, other):
        """Adding rectangles"""
        c = self.a + other.a
        d = self.b + other.b
        return Rectangle(c, d)

    def __sub__(self, other):
        """Subtracting rectangles"""
        p1 = 2 * (self.a + self.b)
        p2 = 2 * (other.a + other.b)
        if p1 > p2 :
            c = self.a - other.a
            d = self.b - other.b
        else:
            c = other.a - self.a
            d = other.b - self.b
        return Rectangle(c,d)
    
    def __str__(self):
        return f'{self.a}x{self.b}'

    def __eq__(self, other):
        """Checking for equality of rectangles"""
        if self.a * self.b == other.a * other.b:
            return True
        else : 
            return False

    def __lt__(self, other):
        """Comparison left less"""
        if self.a * self.b < other.a * other.b:
            return True
        else: 
            return False

    def __le__(self, other):
        """Comparison right less"""
        if self.a * self.b > other.a * other.b: 
            return True
        else: 
            return False

# pr1 = Rectangle(-5, 7)
# pr1 = Rectangle('gtr', 7)
pr1 = Rectangle(1, 7)
pr2 = Rectangle(5, 2)
print("Первый прямоугольник: ", pr1)
print("Первый прямоугольник: ", pr2)
print(pr1 == pr2)
print(pr1 > pr2)