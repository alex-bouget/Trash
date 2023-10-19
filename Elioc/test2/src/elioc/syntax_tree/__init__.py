from .syntax_node import EliocSyntaxNode, EliocSyntaxSubTypeEnum
from .syntax_alternate import EliocSyntaxAlternate
from typing import List, Dict

class EliocSyntaxTree:
    """Elioc syntax tree."""
    root: EliocSyntaxNode
    includer: List[str]
    alternate: Dict[str, EliocSyntaxAlternate]
    pile: List[EliocSyntaxNode]

    def __init__(self, alternate: List[EliocSyntaxAlternate]) -> None:
        self.includer = []
        self.root = EliocSyntaxNode(EliocSyntaxSubTypeEnum.ROOT, [])
        self.alternate = {}
        for i in alternate:
            self.alternate[i.function_name] = i
        self.pile = [self.root]
    
    def add_after(self, node: EliocSyntaxNode) -> None:
        """Add a node after the root node."""
        if node.syntax_type == EliocSyntaxSubTypeEnum.FUNCTION_CALL:
            if node.node_parameters[0].node_parameters[0] in self.alternate.keys():
                for i in self.alternate[node.node_parameters[0].node_parameters[0]].included:
                    self.includer.append(i)
                node.node_parameters[0].node_parameters[0] = self.alternate[node.node_parameters[0].node_parameters[0]].function_name_moved
        self.pile[-1].add_after(node)
    
    def add_in_pile(self, node: EliocSyntaxNode) -> None:
        """Add a node in the pile."""
        self.pile.append(node)
    
    def del_in_pile(self) -> None:
        """Delete the last node in the pile."""
        self.pile.pop()
    
    def add_include(self, include: str) -> None:
        """Add an include to the tree."""
        self.includer.append(include)
    
    def compile(self) -> str:
        """Compile the tree to C code."""
        code = ""
        for i in self.includer:
            code += f"#include {i}\n"
        code += self.root.compile()
        print(code)
        return code
    
    def __str__(self) -> str:
        return self.root.__str__()