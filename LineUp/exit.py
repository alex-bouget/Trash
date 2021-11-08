from .Interpreter.line import Line


class Exit:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def load_command(self, command_name, *parameters):
        if type(command_name) is str:
            print(self.interpreter.global_variable[command_name].load_command(*parameters))
        else:
            print(command_name.load_command(*parameters))
