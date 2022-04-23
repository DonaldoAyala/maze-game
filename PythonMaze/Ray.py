from Point import *

class Ray:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def draw(self, window, color, pygame):
        pygame.draw.line(window, color, self.position.get_tuple(), ((self.position + (self.direction * 10))).get_tuple())
    
    def set_direction(self, point):
        self.direction = (point - self.position)
        self.direction.normalize()

    def cast(self, wall):
        # Logic for line-line intersection: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        x1, y1 = wall.get_point1_tuple()
        x2, y2 = wall.get_point2_tuple()

        x3, y3 = self.position.get_tuple()
        x4, y4 = (self.position + self.direction).get_tuple()
        denominator = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)

        if denominator == 0:
            return None

        t = ( (x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4) ) / denominator
        u = ( (x1 - x3)*(y1 - y2) - (y1 - y3)*(x1 - x2) ) / denominator

        if 0 <= t <= 1 and u > 0:
            return Point(x1 + t*(x2 - x1), y1 + t*(y2 - y1))

