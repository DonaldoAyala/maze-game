from Point import *

class Wall:
    def __init__(self, start, end):
        self.point1 = start
        self.point2 = end
        self.segment = (start, end)

    def get_point1_tuple(self):
        return self.point1.get_tuple()

    def get_point2_tuple(self):
        return self.point2.get_tuple()

    def draw(self, window, color, pygame):
        pygame.draw.line(window, color, self.point1.get_tuple(), self.point2.get_tuple())

