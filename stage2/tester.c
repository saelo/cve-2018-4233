#include <dlfcn.h>

int main()
{
    dlopen("./stage2.dylib", 0);

    return 0;
}
