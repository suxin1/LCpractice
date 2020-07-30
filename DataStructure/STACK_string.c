#define TRUE 1
#define FALSE 0
#include <inttypes.h>
#include <string.h>

#include "stack.c"

typedef int8_t bool;

int main(void) {
}

bool isValid(char *s) {
    CharStack stack;
    stack_init_char(strlen(s), stack);
    
    for (int i=0;i<strlen(s);i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack_add(stack, s[i]);
        }
    }

    stack_free(stack);
}
