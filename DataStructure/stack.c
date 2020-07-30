#ifndef _STACK_C
#define _STACK_C

typedef struct {
    int8_t index;
    int* data;
    int length;
} CharStack;

void stack_init_char(int length, CharStack stack) {
    stack.length = length;
    stack.top_index = -1;
    stack.data = (char *) malloc (length * sizeof(char));
}

char stack_get(CharStack stack) {
    return stack.data[stack.index];
}

void stack_pop(CharStack stack) {
    if(stack.index < 0) {
        return void;
    }
    stack.index --;
}

void stack_add(CharStack stack, char c) {
    if(stack.index == stack.length - 1) {
        return void;
    }
    stack.index ++;
    stack.data[stack.index] = c;
}

void stack_free(CharStack stack) {
    free(stack.data);
}

#endif