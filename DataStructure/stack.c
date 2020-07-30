#ifndef _STACK_C
#define _STACK_C

#include <stdlib.h>

typedef struct {
    int8_t index;
    int* data;
    int length;
} Stack;

void stack_init(int length, Stack stack) {
    stack.length = length;
    stack.index = -1;
    stack.data = (int *) malloc (length * sizeof(int));
}

int stack_get(Stack stack) {
    if (stack.index < 0) {
        return -1;
    }
    return stack.data[stack.index];
}

void stack_pop(Stack stack) {
    if(!(stack.index < 0)) {
        stack.index --;
    }
}

void stack_add(Stack stack, char c) {
    if(!(stack.index == stack.length - 1)) {
        stack.index ++;
        stack.data[stack.index] = c;
    }
}

void stack_free(Stack stack) {
    free(stack.data);
}

#endif
