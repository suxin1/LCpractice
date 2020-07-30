#define TRUE 1
#define FALSE 0
#include <inttypes.h>
#include <string.h>
#include <stdio.h>

#include "stack.c"

typedef int8_t bool;


bool isValid(char *s);
void function(char *s);
int main(void) {
    printf("start\n");
    char *s = "(((())))";
    function(s);
    bool res = isValid(s);
    printf("res:%d", res);
}

void function(char *s) {
    int a = (int)strlen(s);
    printf("length: %d\n", a);
}


bool isValid(char *s) {
    printf(">>>>>------------>\n");
    Stack stack;
    stack_init(strlen(s), stack);
    printf(">>>>>------------>\n");
    for (int i=0;i<strlen(s);i++) {
        printf("----%d\n", i);
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack_add(stack, s[i]);
            continue;
        }
        if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
            int prev = stack_get(stack);
            printf("stack out value: %d\n", prev);
            if(prev < 0) {
                return FALSE;
            }
            char temp_c = (char)prev;
            printf("stack out char: %c\n", temp_c);
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
