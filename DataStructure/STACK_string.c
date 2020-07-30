#define TRUE 1
#define FALSE 0
#include <inttypes.h>
#include <string.h>
#include <stdio.h>

#include "stack.c"

typedef int8_t bool;


bool isValid(char *s);

int main(void) {
    printf("start\n");
    bool res = isValid("(((())))");
    printf("%d", res);
}

bool isValid(char *s) {
    Stack stack;
    stack_init(strlen(s), stack);

    for (int i=0;i<strlen(s);i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack_add(stack, s[i]);
            continue;
        }
        if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
            int prev = stack_get(stack);
            if(prev < 0) {
                return FALSE;
            }
            char temp_c = (char)prev;
            if (s[i] == ')' && temp_c == '(') {
                continue;
            }
            else if (s[i] == '}' && temp_c == '{') {
                continue;
            } else if (s[i] == ']' && temp_c == '[') {
                continue;
            }
        }
        return stack.index < 0;
    }

    stack_free(stack);
    return stack.index < 0;
}
