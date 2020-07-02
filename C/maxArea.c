#define true 1
#define false 0

#include <stdio.h>
#include <string.h>

typedef unsigned int bool;


int maxArea(int* height, int heightSize);

int main(void) {
    int heights[9] = {1,8,6,2,5,4,8,3,7};
    printf("start\n");
    int area = maxArea(heights, 9);
    printf("result: %d", area);
}


int maxArea(int* height, int heightSize){
    if(heightSize == 2) return height[0]*height[1];
    int i = 0, j = heightSize - 1;
    int area = (j-i) * (height[i]<height[j]?height[i]:height[j]);
    while(i<j) {
        if(height[i]<height[j]) {
            i++;
        } else {
            j--;
        }
        int tempA = (j-i) * (height[i]<height[j]?height[i]:height[j]);
        if(tempA > area) area = tempA;
    }
    return area;
}