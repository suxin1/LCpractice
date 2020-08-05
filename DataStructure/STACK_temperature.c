#include "stack.c"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define LEN(A) sizeof(A)/sizeof(A[0])

int* dailyTemperature(int* T, int* answer, int arr_size);

int* printArray(int* T, int size) {
    for (int i=0;i<size;i++) {
        printf("%d,", T[i]);
    }
    printf("\n");
}

int main(void) {
    int a[4] = {74, 72, 75, 77};
    int b[6] = {0};
    dailyTemperature(a, b, 4);
    printArray(b, 4);
}


/**
 * 根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
 * 解决方法：
 *     1.维护一个单调栈，这个栈储存需要观测的温度索引。遍历温度列表，如果栈为空则将其推进栈中。
 *     2.如果当前温度T[i] > 栈中顶部索引温度T[prev_index], 移除顶部索引 prev_index，算出 answer[prev_index] = i - prev_index。重复此步骤，直到栈为空。
 */
int* dailyTemperature(int* T, int* answer, int arr_size) {
    memset(answer, 0, sizeof(int) * arr_size);
    Stack stack;
    stack_init(arr_size, &stack);
    
    for (int i=0;i<arr_size;i++) {
        while (!stack_isEmpty(stack) ) {
            int prev_index = stack_get(stack);
            if (T[i] > T[prev_index]) {
                stack_pop(&stack);
                answer[prev_index] = i - prev_index;
            } else {
                break;
            }
        }
        stack_add(&stack, i);
    }
}
