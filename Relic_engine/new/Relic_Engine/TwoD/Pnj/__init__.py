from ..Character import Character


class Pnj2d(Character):
    def __init__(self):
        self.resolution = 64
        self.map_speed = 0
        self.map_coord = [0, 0]