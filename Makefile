CFLAGS = --std=c11 -Wall -Wextra -pedantic

elioc_var=src/elioc/elioc_var.h src/elioc/elioc_var.o

main: src/main.o $(elioc_var)


clean:
	find . -type f -name '*.o' -delete;
	if [ -f somme ]; then rm somme; fi;