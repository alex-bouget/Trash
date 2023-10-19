from elioc.compile.decoder import *

class PythonDecoder(Decoder):
    def __init__(self, code: str, folder_constructor: str) -> None:
        super().__init__(code, folder_constructor)

    def decode(self):