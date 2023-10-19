#include "elioc/elioc_var.h"

void main(void) {
    elioc_var_init();
    elioc_var_pile();
    elioc_var_new(0, 1);
    elioc_var_set(1, 1);
    elioc_var_get(1);
    elioc_var_unpile();
    elioc_var_shutdown();
}