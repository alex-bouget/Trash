from enum import Enum
from .sub_type import EliocSyntaxSubTypeEnum
from .type_class import EliocSyntaxTypeClass

class EliocSyntaxTypeEnum(Enum):
    """Elioc syntax_type"""
    FUNCTION = EliocSyntaxTypeClass(
        "FUNCTION",
        EliocSyntaxSubTypeEnum.FUNCTION,
        [[EliocSyntaxSubTypeEnum.FUNCTION_PARAMETER, EliocSyntaxSubTypeEnum.RETURN, EliocSyntaxSubTypeEnum.STATEMENT]],
    )
    FOR = EliocSyntaxTypeClass(
        "FOR",
        EliocSyntaxSubTypeEnum.STATEMENT,
        [[EliocSyntaxSubTypeEnum.ASSIGNMENT, EliocSyntaxSubTypeEnum.CONDITION, EliocSyntaxSubTypeEnum.STATEMENT, EliocSyntaxSubTypeEnum.STATEMENT]],
    )
    WHILE = EliocSyntaxTypeClass(
        "WHILE",
        EliocSyntaxSubTypeEnum.STATEMENT,
        [[EliocSyntaxSubTypeEnum.CONDITION, EliocSyntaxSubTypeEnum.STATEMENT]],
    )
    IF = EliocSyntaxTypeClass(
        "IF",
        EliocSyntaxSubTypeEnum.STATEMENT,
        [[EliocSyntaxSubTypeEnum.CONDITION, EliocSyntaxSubTypeEnum.STATEMENT, EliocSyntaxSubTypeEnum.STATEMENT]],
    )
    ELSE = EliocSyntaxTypeClass(
        "ELSE",
        EliocSyntaxSubTypeEnum.STATEMENT,
        [[EliocSyntaxSubTypeEnum.STATEMENT]],
    )