#ifndef ELIOC_VAR_H
#define ELIOC_VAR_H

#include "./elioc_root.h"

void elioc_var_init(void);

void elioc_var_shutdown(void);

void elioc_var_pile(void);

void elioc_var_unpile(void);

void elioc_var_new(byte *name, byte *size);

void elioc_var_delete(byte *name);

byte* elioc_var_set(byte *name, byte *value);

void elioc_var_get(byte *name);



#endif