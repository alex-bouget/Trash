class Exit:
    def __init__(self, interpreter, e_type):
        self.interpreter = interpreter
        self.e_type = e_type

    def load_command(self, command_name, *parameters):
        if type(command_name) is str:
            com = self.interpreter.global_variable[command_name].load_command(*parameters)
        else:
            com = command_name.load_command(*parameters)
        if self.e_type == "print":
            print(com)
        else:
            return ["/L_e*/", com]
