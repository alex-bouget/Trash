from typing import List

from .variable import Variables
from .argument import Argument


class Function:
    scope: List[Variables] = []
    parameters: List[Variables]
    returned: Variables

    function_data: List[Argument]
    needed: List[Argument]


    def __init__(self, parameters: List[Variables], returned: Variables) -> None:
        self.parameters = parameters
        self.returned = returned
        self.function_data = []
        self.needed = []
    
    def decode_function(self, code: str) -> None:
        for i in code.split("\n"):
            if i == "":
                continue
            self.function_data.append(Argument(i, self.scope))