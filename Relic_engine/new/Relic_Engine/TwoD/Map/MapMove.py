from ..Moving.MultipleMove import MultipleMove
from ...variables import Main, Camera


class MapMoving(MultipleMove):
    def __init__(self, map_class):
        self._map_class = map_class
        super().__init__(self._map_class.resolution, self._map_class.map_speed, "World_tile_set")

    def move_left(self, *evt):
        # +x
        if [self.map_coord[0] + 1, self.map_coord[1]] not in self._map_class.collision:
            self._move_left(evt)

    def move_right(self, *evt):
        # -x
        if [self.map_coord[0] - 1, self.map_coord[1]] not in self._map_class.collision:
            self._move_right(evt)

    def move_up(self, *evt):
        # +y
        if [self.map_coord[0], self.map_coord[1] + 1] not in self._map_class.collision:
            self._move_up(evt)

    def move_down(self, *evt):
        # -y
        if [self.map_coord[0], self.map_coord[1] - 1] not in self._map_class.collision:
            self._move_down(evt)

    def teleport_map(self, x=0, y=0):
        for tiles_width in self._map_class.tiles:
            for tiles in tiles_width:
                Main.relic_engine.coords(tiles[1],
                                         (self._map_class.resolution * (tiles[2][0] + x)) // 2 + Camera.cam_x,
                                         (self._map_class.resolution * (tiles[2][1] + y)) // 2 + Camera.cam_y)
