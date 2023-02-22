import micro_process
import json
import os


class Extensions:
    def __init__(self, efs):
        self.efs = json.load(open(efs))
        self.process = micro_process.MicroProcess(os.path.join(os.path.dirname(efs),
                                                               self.efs["launch"]))

    def get_from_process(self):
        t = self.process.get_out()
        while t is None:
            t = self.process.get_out()
        return t

    def get_from_process_without(self):
        return self.process.get_out()

    def send_to_process(self, arg):
        self.process.send_line(arg)
