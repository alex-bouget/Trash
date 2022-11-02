from typing import List

class EliocSyntaxAlternate:
    """Elioc syntax alternate. Move a function to a c or elioc function."""
    function_name: str
    function_name_moved: str
    included: List[str]

    def __init__(self, function_name: str, function_name_moved: str, included: List[str]) -> None:
        self.function_name = function_name
        self.function_name_moved = function_name_moved
        self.included = included