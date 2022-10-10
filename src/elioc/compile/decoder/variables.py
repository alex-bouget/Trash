from typing import List
from .argument import Argument

class Variable:
    name: str
    type: str
    start_value: Argument
    new_value: List[Argument]

    def __init__(self, name: str, type: str, start_value: Argument) -> None:
        self.name = name
        self.type = type
        self.start_value = start_value
    
    def change_value(self, new_value: Argument) -> None:
        self.new_value.append(new_value)
    
    def create(self) -> str:
        return f"{self.type} {self.name} = {self.start_value};"
    
    def update(self) -> str:
        return f"{self.name} = {self.new_value};"