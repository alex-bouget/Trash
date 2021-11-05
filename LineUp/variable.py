class Variable:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def load_command(self, command_name, *parameters):
        self.interpreter.global_variable[command_name] = \
            self.interpreter.global_class[parameters[0]]()
