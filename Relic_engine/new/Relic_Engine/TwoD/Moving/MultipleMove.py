from ...variables import Main


class MultipleMove:
    def __init__(self, resolution, map_speed, tags_or_id_move):
        self.resolution = resolution
        self.speed = map_speed
        self.mover = tags_or_id_move
        self.map_coord = [0, 0]
        self.move_lock = False

    def countdown(self):
        return int(self.resolution / self.speed)

    def rest(self):
        return self.resolution - (int(self.resolution / self.speed) * self.speed)

    def _move_left(self, *evt):
        # +x
        if not self.move_lock:
            Main.windows.after(10, lambda: self.move_anim(self.speed, 0, self.countdown(), self.rest(), 10))
            self.map_coord[0] += 1

    def _move_right(self, *evt):
        # -x
        if not self.move_lock:
            Main.windows.after(10, lambda: self.move_anim(-self.speed, 0, self.countdown(), -(self.rest()), 10))
            self.map_coord[0] -= 1

    def _move_up(self, *evt):
        # +y
        if not self.move_lock:
            Main.windows.after(10, lambda: self.move_anim(0, self.speed, self.countdown(), self.rest(), 10))
            self.map_coord[1] += 1

    def _move_down(self, *evt):
        # -y
        if not self.move_lock:
            Main.windows.after(10, lambda: self.move_anim(0, -self.speed, self.countdown(), -(self.rest()), 10))
            self.map_coord[1] -= 1

    def move_anim(self, x, y, countdown, rest, time):
        self.move_pixel_map(x // 2, y // 2)
        if countdown > 1:
            self.move_lock = True
            Main.windows.after(time,
                               lambda x_a=x, y_a=y, countdown_a=countdown - 1, rest_a=rest, time_a=time:
                               self.move_anim(x_a, y_a, countdown_a, rest_a, time_a))
        elif countdown == 1:
            self.move_lock = False
            if x == 0:
                Main.windows.after(1,
                                   lambda x_a=x, y_a=rest, countdown_a=countdown - 1, rest_a=rest, time_a=time:
                                   self.move_anim(x_a, y_a, countdown_a, rest_a, time_a))
            else:
                Main.windows.after(1,
                                   lambda x_a=rest, y_a=y, countdown_a=countdown - 1, rest_a=rest, time_a=time:
                                   self.move_anim(x_a, y_a, countdown_a, rest_a, time_a))

    def move_pixel_map(self, x=0, y=0):
        Main.relic_engine.move(self.mover, x, y)

    def move_coord_map(self, x=0, y=0):
        self.move_pixel_map(x * self.resolution, y * self.resolution)
