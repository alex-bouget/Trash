from elioc import *
from elioc.syntax_tree.syntax_type import *
from typing import List




def create_c_file(python_file):
    """Create a c file from a python file."""
    alternate = [
        EliocSyntaxAlternate("print", "printf", ["<stdio.h>"])
    ]

    python_data = open(python_file, "r").read()
    tree = EliocSyntaxTree(alternate)
    lines = enumerate(python_data.splitlines())
    for i in lines:
        print(i)
        data = i[1]
        if data == " ":
            continue
        elif data.startswith("def"):
            in_statement = True
            name = data.split("def ")[1].split("(")[0].strip()
            parameter_data = data.split("def")[1].split("(")[1].split(")")[0]
            parameter_data = parameter_data.split(",") if parameter_data != "" else []
            parameters = [i.split(": ") for i in parameter_data] 

            returned = data.split("->")[1].split(":")[0].strip()

            variable = []
            for i in parameters:
                i[1] = i[1] if i[1] != "str" else "char*"
                variable.append(EliocSyntaxNode(EliocSyntaxSubTypeEnum.VARIABLE, [i[1], i[0]]))
            
            function_name = EliocSyntaxNode(EliocSyntaxSubTypeEnum.FUNCTION_NAME, [name])
            function_parameters = EliocSyntaxNode(EliocSyntaxSubTypeEnum.FUNCTION_PARAMETER, variable)
            function_return = EliocSyntaxNode(EliocSyntaxSubTypeEnum.RETURN, [returned])
            function_body = EliocSyntaxNode(EliocSyntaxSubTypeEnum.STATEMENT, [])

            function_data = EliocSyntaxNode(EliocSyntaxTypeEnum.FUNCTION, [function_name, function_parameters, function_return, function_body])
            tree.add_after(function_data)
            tree.add_in_pile(function_data)
        elif "=" in data:
            name = data.split("=")[0].split(":")[0].strip()
            typing = data.split("=")[0].split(":")[1].strip()
            value = data.split("=")[1].strip()
            typing = typing if typing != "str" else "char*"
            variable = EliocSyntaxNode(EliocSyntaxSubTypeEnum.VARIABLE, [typing, name])
            constant = EliocSyntaxNode(EliocSyntaxSubTypeEnum.CONSTANT, [value])
            assignment = EliocSyntaxNode(EliocSyntaxSubTypeEnum.ASSIGNMENT, [variable, constant])
            tree.add_after(assignment)
        elif "(" in data and ")" in data:
            name = data.split("(")[0].strip()
            parameter_data = data.split("(")[1].split(")")[0]
            parameter_data = parameter_data.split(",") if parameter_data != "" else []
            parameters = []
            for i in parameter_data:
                if (i.startswith('"') and i.endswith('"')) or i.isnumeric() or i.isdecimal():
                    parameters.append(EliocSyntaxNode(EliocSyntaxSubTypeEnum.CONSTANT, [i]))
                else:
                    parameters.append(EliocSyntaxNode(EliocSyntaxSubTypeEnum.VARIABLE, [i]))
            function_name = EliocSyntaxNode(EliocSyntaxSubTypeEnum.FUNCTION_NAME, [name])
            function_parameters = EliocSyntaxNode(EliocSyntaxSubTypeEnum.FUNCTION_PARAMETER, parameters)
            function_call = EliocSyntaxNode(EliocSyntaxSubTypeEnum.FUNCTION_CALL, [function_name, function_parameters])
            tree.add_after(function_call)
        elif data == "":
            tree.del_in_pile()
            pass
    print(tree)
    open("test.c", "w").write(tree.compile())

create_c_file("exemple/print.py")