from .sub_type import EliocSyntaxSubTypeEnum
from typing import List

class EliocSyntaxTypeClass:
    """Base class for Elioc syntax type classes."""
    name: str
    syntax_type: EliocSyntaxSubTypeEnum
    child: List[EliocSyntaxSubTypeEnum]
    return_type: type

    def __init__(self, name: str, syntax_type: EliocSyntaxSubTypeEnum, child: List[List[EliocSyntaxSubTypeEnum]], return_type: type = None):
        self.name = name
        self.syntax_type = syntax_type
        self.child = child
        self.return_type = return_type