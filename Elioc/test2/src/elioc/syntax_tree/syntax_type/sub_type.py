from enum import Enum

class EliocSyntaxSubTypeEnum(Enum):
    STATEMENT = (1, None)
    CONDITION = (2, bool)
    RETURN = (3, type)
    FUNCTION = (4, None)
    FUNCTION_PARAMETER = (5, None)
    ASSIGNMENT = (6, None)
    CALCULATION = (7, None)
    VARIABLE = (8, None)
    CONSTANT = (9, None)
    FUNCTION_CALL = (10, None)
    FUNCTION_NAME = (11, None)
    ROOT = (12, None)