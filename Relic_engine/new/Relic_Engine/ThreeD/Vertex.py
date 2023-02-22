import math
from .Axis import Axis3


class Vertex:
    def __init__(self, point):
        self.point = Axis3(*point)

    def flatten(self, scale, distance):
        # calculate 2D coordinates from 3D point
        projected_y = int(((self.point.y * distance) / (self.point.z + distance)) * scale)
        projected_x = int(((self.point.x * distance) / (self.point.z + distance)) * scale)
        return [projected_x, projected_y]

    def rotate(self, axis, angle):
        angle = angle / 450 * 180 / math.pi
        if axis == 'z':
            new_x = self.point.x * math.cos(angle) - self.point.y * math.sin(angle)
            new_y = self.point.y * math.cos(angle) + self.point.x * math.sin(angle)
            new_z = self.point.z
        elif axis == 'x':
            new_y = self.point.y * math.cos(angle) - self.point.z * math.sin(angle)
            new_z = self.point.z * math.cos(angle) + self.point.y * math.sin(angle)
            new_x = self.point.x
        elif axis == 'y':
            new_x = self.point.x * math.cos(angle) - self.point.z * math.sin(angle)
            new_z = self.point.z * math.cos(angle) + self.point.x * math.sin(angle)
            new_y = self.point.y
        else:
            raise ValueError('invalid rotation axis')
        del self.point
        self.point = Axis3(new_x, new_y, new_z)

    def move(self, axis, value):
        if axis == 'x':
            self.point.x += value
        elif axis == 'y':
            self.point.y += value
        elif axis == 'z':
            self.point.z += value
        else:
            raise ValueError('Invalid movement axis')
