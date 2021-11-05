class Exit:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def load_command(self, command_name, *parameters):
        print(self.interpreter.global_variable[command_name].load_command(*parameters))
