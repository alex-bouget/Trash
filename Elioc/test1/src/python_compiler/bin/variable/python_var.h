#ifndef PYTHON_VAR_H
#define PYTHON_VAR_H

/*
type:
5: int
6: float
7: string
8: bool
7: object
*/

struct pythonVar {
    char type;
    void *value;
    int size;
};

struct pythonVar *pythonVar_new(char type, void *value, int size);

void pythonVar_free(struct pythonVar *var);

void pythonVar_set(struct pythonVar *var, char type, void *value, int size);

void* pythonVar_get(struct pythonVar *var, int* size);

#endif