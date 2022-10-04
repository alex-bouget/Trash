from typing import Dict, List, Tuple
from .variableValue import VariableValue

class Variables:
    all_variables: Dict[str, Tuple[int, List[VariableValue]]] = {}
    folder_constructor: str

    def __init__(self, folder_constructor) -> None:
        self.folder_constructor = folder_constructor
    
    def add_variable(self, name: str, type_var: str) -> None:
        if name in self.all_variables:
            raise Exception(f"Variable {name} already exists in scope")
        else:
            self.all_variables[name] = [hash(name), [type_var]]
    
    def set_variable(self, name: str, value: str) -> None:
        if name in self.all_variables:
            self.all_variables[name][1].append(VariableValue(value))