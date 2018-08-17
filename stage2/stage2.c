#include <stdlib.h>
#include <stdio.h>

__attribute__((constructor))
void _injection()
{
    // Dummy .dylib
    puts("Hello World!");
}
