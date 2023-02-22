class Exec:
    def load_command(self, command_name, *parameters):
        return getattr(self, command_name)(*parameters)
