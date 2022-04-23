class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, window, color, pygame):
        pygame.draw.circle(window, color, self.get_tuple(), 5)

    def from_tuple(tuple):
        return Point(tuple[0], tuple[1])

    def get_tuple(self):
        return (self.x, self.y)

    def normalize(self):
        self.x, self.y = (Point(self.x, self.y) / ((self.x ** 2 + self.y ** 2) ** (1/2))).get_tuple()
    
    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)
    
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)
    
    def __str__(self):
        return str((self.x, self.y))