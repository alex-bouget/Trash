import pytmx
from .MapTileSet import MapTileSet
from ...variables import Main, Camera
from .MapMove import MapMoving


class Map2D:
    def __init__(self):
        self.map_load = ""
        self.resolution = 0
        self.collision_layer = ""
        self.collision = []
        self.layer = []
        self.Map_sys = MapTileSet()
        self.map_speed = 8
        self.tiles = []
        self.MapMove = MapMoving(self)
        Main.relic_engine.reload_function["Relic-2dCore-Map"] = lambda: self.MapMove.teleport_map(
            self.MapMove.map_coord[0], self.MapMove.map_coord[1])

    def set_map_settings(self, **args):
        if "collision" in args:
            self.collision_layer = args["collision"]
        if "resolution" in args:
            self.resolution = args["resolution"]
            self.MapMove.resolution = self.resolution
        if "layer" in args:
            self.layer = []
            for layer in args["layer"]:
                self.layer.append(layer)
        if "speed" in args:
            self.map_speed = args["speed"]

    def load_tmx_map(self, tmx_file):
        tiled_map = pytmx.TiledMap(tmx_file)
        self.map_load = ["tmx_map", tmx_file]
        layer_tile = []
        for layer_name in self.layer:
            layer_tile.append(tiled_map.get_layer_by_name(str(layer_name)).tiles())
        for tile in layer_tile:
            self.tiles.append([])
            for x, y, image in tile:
                self.tiles[-1].append([])
                self.tiles[-1][-1].append(self.Map_sys.tiles_load(image[0], image[1]))
                self.tiles[-1][-1].append(
                    Main.relic_engine.create_image(
                        (self.resolution * x)//2 + Camera.cam_x,
                        (self.resolution * y)//2 + Camera.cam_y,
                        anchor="center",
                        image=self.tiles[-1][-1][0],
                        tags="World_tile_set"
                    )
                )
                self.tiles[-1][-1].append([x, y])
        self.collision = []
        if self.collision_layer != "":
            for x, y, image in tiled_map.get_layer_by_name(self.collision_layer).tiles():
                self.collision.append([-x, -y])

    def unload_map(self):
        Main.relic_engine.delete("World_tile_set")
        del self.tiles
        self.tiles = []
