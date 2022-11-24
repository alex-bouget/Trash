#include "elioc_var.h"
#include "elioc_root.h"
#include <err.h>
#include <stdlib.h>

#define ELIOC_VAR_MAX 255
#define ELIOC_PILE_MAX 255


byte** elioc_data = NULL;
int elioc_data_size = 0;
byte* elioc_pile_now = NULL;

void elioc_var_init() {
    if (elioc_data != NULL) {
        elioc_var_shutdown();
    }
    elioc_data = malloc(sizeof(byte*)*ELIOC_PILE_MAX); // 255 pile memory locations
    for (int i = 0; i < ELIOC_PILE_MAX; i++) {
        elioc_data[i] = NULL;
    }
}

void elioc_var_shutdown() {
    for (int i = 0; i < ELIOC_PILE_MAX; i++) {
        if (elioc_data[i] != NULL) {
            free(elioc_data[i]);
        }
    }
    free(elioc_data);
}

void elioc_var_pile() {
    if (elioc_data_size < ELIOC_VAR_MAX) {
        elioc_pile_now = malloc(sizeof(byte*)*ELIOC_VAR_MAX); // 255 pile memory locations
        elioc_data[elioc_data_size] = elioc_pile_now;
        elioc_data_size++;
        return;
    }
    err(63, "Pile overflow: your program has too many piles");
}

void elioc_var_unpile() {
    if (elioc_data_size > 0) {
        free(elioc_pile_now);
        elioc_data_size--;
        return;
    }
    err(64, "Pile underflow: your program has too few piles");
}

void elioc_var_new(byte *name, byte *size) {
    (void*)name;
    (void*)size;
}

void elioc_var_delete(byte *name) {
    (void*)name;
}

byte* elioc_var_set(byte *name, byte *value) {
    (void*)name;
    (void*)value;
    return NULL;
}

void elioc_var_get(byte *name) {
    (void*)name;
}