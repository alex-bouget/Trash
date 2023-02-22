from .interpreter import Interpreter
from .module import load_modules, decode_modules


class LineUp(Interpreter):
    def __init__(self, m_dir, lum, e_type):
        load_modules(m_dir, lum)
        super(LineUp, self).__init__(decode_modules(), e_type)