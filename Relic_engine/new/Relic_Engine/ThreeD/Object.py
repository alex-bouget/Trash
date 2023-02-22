"""
Relic_Engine 3D-Script
Test for 3D Object
"""
import tkinter
from .Vertex import Vertex
from ..variables import Main


class Face:
    def __init__(self, vertices):
        self.a, self.b, self.c, self.color = vertices


class Object:
    def __init__(self, point, triangles):
        self.master = Main.relic_engine
        self.data_object = []
        self.point = []
        self.distance = 6
        self.scale = 100
        self.writePoints(point)
        self.writeTriangles(triangles)

    def writePoints(self, points):
        self.points = []
        for point in points:
            self.points.append(Vertex(point))

    def writeTriangles(self, triangles):
        self.triangles = []
        for triangle in triangles:
            if len(triangle) != 4:
                triangle.append('gray')
            self.triangles.append(Face(triangle))

    def createTriangle(self, points, color):
        a, b, c = points[0], points[1], points[2]
        # create coordinates starting in center of screen
        coord = [a[0] + self.zero[0],
                 a[1] + self.zero[1],
                 b[0] + self.zero[0],
                 b[1] + self.zero[1],
                 c[0] + self.zero[0],
                 c[1] + self.zero[1]]
        # draw triangle on screen
        self.data_object.append(self.master.create_polygon(coord, fill=color, outline="black"))

    def createLine(self, points, color):
        a, b = points[0], points[1]
        self.data_object.append(self.master.create_line(a[0], a[1], b[0], b[1], fill=color, arrow=tkinter.BOTH))
        return self.data_object[-1]

    def clear(self):
        # clear display
        self.master.delete(*self.data_object)
        del self.data_object
        self.data_object = []

    def delete(self, item):
        self.master.delete(item)
        return None

    def after(self, time, function):
        self.master.after(time, function)

    def render(self):
        self.zero = [int(Main.x / 2), int(Main.y / 2)]
        self.flattened = []
        for point in self.points:
            self.flattened.append(point.flatten(self.scale, self.distance))

        triangles = []
        for triangle in self.triangles:
            avg_z = -(self.points[triangle.a].point.z + self.points[triangle.b].point.z +
                      self.points[triangle.c].point.z) / 3
            triangles.append((self.flattened[triangle.a], self.flattened[triangle.b], self.flattened[triangle.c],
                              triangle.color, avg_z))

        # sort triangles from furthest back to closest
        triangles = sorted(triangles, key=lambda x: x[4])

        # draw triangles
        for triangle in triangles:
            self.createTriangle(triangle[0:3], triangle[3])

    def rotate(self, axis, angle):
        # rotate model around axis
        for point in self.points:
            point.rotate(axis, angle)
