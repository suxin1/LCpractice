#ifndef _STACK_C
#define _STACK_C

#include <stdlib.h>
#include <stdio.h>

// stack 结构体
typedef struct {
    int index;
    int length;
    int* data;
} Stack;

void stack_init(int length, Stack *stack) {
    stack -> length = length;
    stack -> index = -1;
    stack -> data = (int *) malloc (length * sizeof(int));
}

int stack_isEmpty(Stack stack) {
    return stack.index < 0;
}

int stack_get(Stack stack) {
    /**
     * 调用 stack_get 之前需调用 stack_isEmpty 判断是否为空。
     * */
    return stack.data[stack.index];
}

void stack_pop(Stack *stack) {
    if(!(stack -> index < 0)) {
        stack -> index --;
    }
}

void stack_add(Stack *stack, int c) {
    if(!(stack -> index == stack -> length - 1)) {
        printf("index: %d, add %d\n", stack -> index, c);
        stack -> index ++;
        stack -> data[stack -> index] = c;
    }
}

void stack_free(Stack stack) {
    /** 
     * stack 内存清理。
     * */
    free(stack.data);
    stack.data = NULL;
}

#endif
