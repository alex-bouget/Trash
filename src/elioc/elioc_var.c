#include "elioc_var.h"
#include "elioc_root.h"
#include <err.h>
#include <stdlib.h>

#define MEMORY_DISK_MAX 255
#define MEMORY_MAX 255


struct elioc_var*** memory_disk = NULL;
byte disk_size = 0;
struct elioc_var** memory_now = NULL;

void elioc_var_init() {
    if (memory_disk != NULL) {
        elioc_var_shutdown();
    }
    memory_disk = malloc(sizeof(byte*)*MEMORY_DISK_MAX); // 255 pile memory locations
    for (int i = 0; i < MEMORY_DISK_MAX; i++) {
        memory_disk[i] = NULL;
    }
}

void elioc_var_shutdown() {
    for (int i = 0; i < MEMORY_DISK_MAX; i++) {
        if (memory_disk[i] != NULL) {
            free(memory_disk[i]);
        }
    }
    free(memory_disk);
}

void elioc_var_pile() {
    if (disk_size < MEMORY_MAX) {
        memory_now = malloc(sizeof(struct elioc_var**)*MEMORY_MAX); // 255 pile memory locations
        for (int i = 0; i < MEMORY_MAX; i++) {
            memory_now[i] = NULL;
        }
        memory_disk[disk_size] = memory_now;
        disk_size++;
        return;
    }
    err(63, "Pile overflow: your program has too many piles");
}

void elioc_var_unpile() {
    if (disk_size > 0) {
        free(memory_now);
        disk_size--;
        memory_disk[disk_size] = NULL;
        memory_now = memory_disk[disk_size-1];
        return;
    }
    err(64, "Pile underflow: your program has too few piles");
}

void elioc_var_new(byte *name, byte *size) {
    if (memory_now == NULL) {
        err(65, "No pile: you need a pile");
    }
    if (&memory_now[*name] != NULL) {
        err(66, "Variable already exists");
    }
    struct elioc_var new_var = {
        .size = *size,
        .data = malloc(sizeof(byte)*(*size))
    };
    memory_now[*name] = &new_var;
}

void elioc_var_delete(byte *name) {
    if (memory_now == NULL) {
        err(65, "No pile: you need a pile");
    }
    if (&memory_now[*name] == NULL) {
        err(67, "Variable does not exist");
    }
    free(memory_now[*name]->data);
    free(memory_now[*name]);
    memory_now[*name] = NULL;
}


void elioc_var_set(byte *name, byte* size_entry, byte *value) {
    if (memory_now == NULL) {
        err(65, "No pile: you need a pile");
    }
    if (&memory_now[*name] == NULL) {
        err(67, "Variable does not exist");
    }
    if (memory_now[*name]->size <= *size_entry) {
        err(68, "Variable size mismatch");
    }
    memory_now[*name]->data[*size_entry] = *value;
}

struct elioc_var* elioc_var_get(byte *name) {
    if (memory_now == NULL) {
        err(65, "No pile: you need a pile");
    }
    if (&memory_now[*name] == NULL) {
        err(67, "Variable does not exist");
    }
    return memory_now[*name];
}

#ifdef ELIOC_DEBUG

#include <assert.h>

int main() {
    elioc_var_init();
    elioc_var_pile();
    assert (disk_size == 1);
    elioc_var_pile();
    assert (disk_size == 2);
    elioc_var_unpile();
    assert (disk_size == 1);
    elioc_var_unpile();
    elioc_var_shutdown();
    return EXIT_SUCCESS;
}

#endif