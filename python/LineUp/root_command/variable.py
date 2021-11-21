class Variable:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def load_command(self, command_name, name, globale=""):
        if globale == "global":
            self.interpreter.global_variable[command_name] = \
                self.interpreter.global_class[name](self.interpreter.global_variable,
                                                    self.interpreter.global_class)
        else:
            self.interpreter.global_variable[command_name] = \
                self.interpreter.global_class[name]()
