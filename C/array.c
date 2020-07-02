/**
 * 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
 * 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
 * 说明:
 * 返回的下标值（index1 和 index2）不是从零开始的。
 * 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
*/
#include <stdlib.h>
#include <stdio.h>

int* twoSum(int* numbers, int numbersSize, int target, int* returnSize);

int main() {
    int numbers[4] = {2, 7, 11, 15};
    int* sum;
    sum = twoSum(numbers, 2, 9, numbers);
    printf("%d", sum[1]);
    free(sum); 
}

int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int i = 0,j = numbersSize - 1;
    *returnSize = 2;
    int* res = (int *) malloc(sizeof(int) * 2);
    while(i<j) {
        if(numbers[i] + numbers[j] == target) {
            break;
        } else if (numbers[i] + numbers[j] < target) {
            i++;
        } else {
            j--;
        }
    }
    res[0] = ++i;
    res[1] = ++j;
    return res;
}
