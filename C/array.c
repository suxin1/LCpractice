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
