class Exec:
    def __init__(self):
        self.command = {}

    def load_command(self, command_name, *parameters):
        return self.command[command_name](*parameters)
