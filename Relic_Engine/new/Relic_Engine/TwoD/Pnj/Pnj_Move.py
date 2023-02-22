from ..Moving.MultipleMove import MultipleMove


class PnjMove(MultipleMove):
    def __init__(self, pnj_class):
        self._pnj_class = pnj_class
        super().__init__(self._pnj_class.reolution, 50, self._pnj_class.id)
        self.move_left = self._move_left
        self.move_right = self._move_right
        self.move_up = self._move_up
        self.move_down = self._move_down
