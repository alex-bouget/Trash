from LineUp.Interpreter import Interpreter
from LineUp import lumodule
from io import StringIO

lumodule.load_modules("lumodule")

data = lumodule.decode_modules()


inter = Interpreter(data)
inter.execute("script exemple/script-exemple.lup")
