CC = clang

.PHONY: all
all: stage2.dylib tester

stage2.dylib: stage2.c $(LIB)
	$(CC) -shared $(CFLAGS) -o stage2.dylib $(LIB) stage2.c

tester: tester.c
	$(CC) -o tester tester.c
