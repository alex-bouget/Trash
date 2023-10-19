#include "python_var.h"
#include <stdlib.h>
#include <string.h>

struct pythonVar *pythonVar_new(char type, void *value, int size)
{
    struct pythonVar *var = malloc(sizeof(struct pythonVar));
    pythonVar_set(var, type, value, size);
    return var;
}
void pythonVar_free(struct pythonVar *var)
{
    free(&var->type);
    free(var->value);
    free(&var->size);
    free(var);
}

void pythonVar_set(struct pythonVar *var, char type, void *value, int size)
{
    var->type = type;
    var->value = value;
    var->size = size;
}

void *pythonVar_get(struct pythonVar *var)
{
    if (var->type == 'i')
    {
        return &var->value;
    }
    else if (var->type == 's')
    {
        char *str = malloc(var->size);
        strcpy(str, var->value);
        return str;
    }
    else if (var->type == 'f')
    {
        return &var->value;
    }
    else if (var->type == 'b')
    {
        return &var->value;
    }
    return NULL;
}
