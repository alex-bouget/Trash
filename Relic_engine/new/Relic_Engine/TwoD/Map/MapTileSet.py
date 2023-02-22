from PIL import ImageTk, Image


class MapTileSet:
    def __init__(self):
        # { "tile_set_name": [{"coord": [0,1], "Image": "img"}}, ...]
        self.tiles = {}  # tile saver

    def tiles_load(self, tile_set, coord=None):
        """
        :param tile_set:
        :param coord:
        :return ImageTk:
        """
        if tile_set in self.tiles.keys():
            for tile_sys in self.tiles[tile_set]:
                if tile_sys["coord"] == coord:
                    return tile_sys["Image"]
            self.tiles[tile_set].append({
                    "coord": coord,
                    "Image": ImageTk.PhotoImage(Image.open(tile_set)
                                                .convert("RGBA")
                                                .crop((coord[0], coord[1], coord[0] + coord[2], coord[1] + coord[3])))
            })
        else:
            self.tiles[tile_set] = [{
                    "coord": coord,
                    "Image": ImageTk.PhotoImage(Image.open(tile_set)
                                                .convert("RGBA")
                                                .crop((coord[0], coord[1], coord[0]+coord[2], coord[1]+coord[3])))
            }]
        return self.tiles[tile_set][-1]["Image"]
