CFLAGS= -g -std=c11 -Wall -Wextra -pedantic -D_XOPEN_SOURCE=700

all: test

test: elioc_var_test

elioc_var_test: src/elioc/elioc_var.c
	gcc $(CFLAGS) -o elioc_var_test src/elioc/elioc_var.c -D ELIOC_DEBUG

%.o: %.c
	gcc -c $(CFLAGS) $<

clean:
	@rm -f elioc_var_test *.o


