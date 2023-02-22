from PIL import Image, ImageTk
from ...variables import Main, Camera
from .Character_Move import CharacterMove


class Character:
    def __init__(self, img, nb_frame, static_map=False):
        self.static_map = static_map
        self.load_character(img, nb_frame)
        self.Character_Move = CharacterMove(self, 100)
        Main.relic_engine.reload_function["Relic-2DCore-Character"] = self.Character_Move.reload_character

    def load_character(self, img, nb_frame):
        try:
            Main.relic_engine.delete(self.character_id)
        except AttributeError:
            pass
        original = Image.open(img)
        if float(original.size[0] / nb_frame) != float(int(original.size[0] / nb_frame)) or\
                float(original.size[1] / 4) != float(int(original.size[1] / 4)):
            raise ValueError("Number of frame unavailable with image size")
        self.height_sprite = original.size[0] / nb_frame
        self.width_sprite = original.size[1] / nb_frame
        self.nbFrame = nb_frame
        self.img = img
        self.Frame = []  # [DOWN, LEFT, RIGHT, UP]
        x = 0
        y = 0
        for strip in range(4):
            strip_image = []
            for frame in range(nb_frame):
                strip_image.append(ImageTk.PhotoImage(Image.open(img).crop((x * self.height_sprite,
                                                                            y * self.width_sprite,
                                                                            (x + 1) * self.height_sprite,
                                                                            (y + 1) * self.width_sprite
                                                                            ))))
                x = x + 1
            x = 0
            y = y + 1
            self.Frame.append(strip_image)
        self.character_id = Main.relic_engine.create_image(Camera.cam_x,
                                                           Camera.cam_y+16,
                                                           anchor="s",
                                                           image=self.Frame[0][0])
