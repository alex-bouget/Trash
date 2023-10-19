from .syntax_type import *


class EliocSyntaxNode:
    """Base class for Elioc syntax nodes."""
    syntax_type: EliocSyntaxTypeEnum or EliocSyntaxSubTypeEnum
    node_parameters: list
    node_children = None

    def __init__(self, syntax_type: EliocSyntaxTypeEnum or EliocSyntaxSubTypeEnum, node_parameters: list or None) -> None:
        self.syntax_type = syntax_type
        self.node_parameters = node_parameters
        self.node_children = None
    
    def add_after(self, node, is_inside: bool =False) -> None:
        """Add a node after this node."""
        if type(self.syntax_type) == EliocSyntaxTypeEnum and not is_inside:
            self.node_parameters[-1].add_after(node)
        else:
            if self.node_children == None:
                self.node_children = node
            else:
                self.node_children.add_after(node, True)
     
    def compile(self) -> str:
        """Compile this node and return the result."""
        my_data = ""
        if self.syntax_type == EliocSyntaxTypeEnum.FUNCTION:
            function_name = self.node_parameters[0].compile()
            function_parameters = self.node_parameters[1].compile()
            function_return = self.node_parameters[2].compile()
            if function_return == "None":
                function_return = "void"
            function_code = self.node_parameters[3].compile()
            print(function_code)
            my_data = "{} {}({}) {{{}}}".format(function_return, function_name, function_parameters, function_code)
            print(my_data)
        elif self.syntax_type == EliocSyntaxSubTypeEnum.FUNCTION_NAME:
            my_data = self.node_parameters[0]
        elif self.syntax_type == EliocSyntaxSubTypeEnum.FUNCTION_PARAMETER:
            my_data = ", ".join([i.compile() for i in self.node_parameters])
        elif self.syntax_type == EliocSyntaxSubTypeEnum.RETURN:
            my_data = self.node_parameters[0]
        elif self.syntax_type == EliocSyntaxSubTypeEnum.ROOT:
            print("root")
        elif self.syntax_type == EliocSyntaxSubTypeEnum.VARIABLE:
            if len(self.node_parameters) == 2:
                my_data = f"{self.node_parameters[0]} {self.node_parameters[1]}"
            else:
                my_data = f"{self.node_parameters[0]}"
        elif self.syntax_type == EliocSyntaxSubTypeEnum.CONSTANT:
            my_data = self.node_parameters[0]
        elif self.syntax_type == EliocSyntaxSubTypeEnum.STATEMENT:
            my_data = ""
        elif self.syntax_type == EliocSyntaxSubTypeEnum.ASSIGNMENT:
            my_data = f"{self.node_parameters[0].compile()} = {self.node_parameters[1].compile()};"
        elif self.syntax_type == EliocSyntaxSubTypeEnum.FUNCTION_CALL:
            my_data = f"{self.node_parameters[0].compile()}({self.node_parameters[1].compile()});"
        else:
            print(self.node_parameters)
            raise Exception("Unknown syntax type." + str(self.syntax_type))
        return my_data + (self.node_children.compile() if self.node_children != None else "")
    
    def __str__(self) -> str:
        """Return the string representation of this node."""
        data = self.syntax_type.name + "-> [" + ", ".join([str(i) for i in self.node_parameters]) + "]"
        data = data.replace("\n", "\n    :")
        node = "\n" + str(self.node_children) if self.node_children else ""
        return data + node