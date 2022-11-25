#ifndef ELIOC_VAR_H
#define ELIOC_VAR_H

#include "./elioc_root.h"

struct elioc_var {
    byte size;
    byte* data;
};

void elioc_var_init(void);

void elioc_var_shutdown(void);

void elioc_var_pile(void);

void elioc_var_unpile(void);

void elioc_var_new(byte *name, byte *size);

void elioc_var_delete(byte *name);

void elioc_var_set(byte *name, byte* size_entry, byte *value);

struct elioc_var* elioc_var_get(byte *name);



#endif