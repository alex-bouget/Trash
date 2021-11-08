from LineUp.Interpreter import Interpreter
from LineUp.module import load_modules, decode_modules

if __name__ == "__main__":
    load_modules("lumodule")

    data = decode_modules()
    inter = Interpreter(data)
    inter.execute("script exemple/script-exemple.lup")
