from ...variables import Main, Camera


class StaticMove:
    def __init__(self, frame, character_id, timer):
        self.Frame = frame
        self.character_id = character_id
        self.timer = timer
        self.move_lock = False

    def _move_left(self, *v):
        if not self.move_lock:
            Main.windows.after(10, lambda animation=self.Frame[1]: self.move_anim(animation, 0))

    def _move_right(self, *v):
        if not self.move_lock:
            Main.windows.after(10, lambda animation=self.Frame[2]: self.move_anim(animation, 0))

    def _move_up(self, *v):
        if not self.move_lock:
            Main.windows.after(10, lambda animation=self.Frame[3]: self.move_anim(animation, 0))

    def _move_down(self, *v):
        if not self.move_lock:
            Main.windows.after(10, lambda animation=self.Frame[0]: self.move_anim(animation, 0))

    def move_anim(self, anim, number):
        try:
            self.move_lock = True
            image = anim[number]
            Main.relic_engine.itemconfigure(self.character_id, image=image)
            Main.windows.after(self.timer, lambda animation=anim, num=number+1: self.move_anim(animation, num))
        except IndexError:
            self.move_lock = False
            Main.relic_engine.itemconfigure(self.character_id, image=anim[0])

    def reload_character(self):
        Main.relic_engine.coords(self.character_id, Camera.cam_x, Camera.cam_y+16)
