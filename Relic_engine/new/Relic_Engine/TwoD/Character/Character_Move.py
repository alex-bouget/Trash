from ..Moving.StaticMove import StaticMove


class CharacterMove(StaticMove):
    def __init__(self, character_class, timer):
        self._class = character_class
        super().__init__(self._class.Frame, self._class.character_id, timer)
        self.move_left = self._move_left
        self.move_right = self._move_right
        self.move_up = self._move_up
        self.move_down = self._move_down
