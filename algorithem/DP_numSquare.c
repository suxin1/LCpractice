#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int numSqures(int n);
void print_size(int a[][3]);

int main() {
    int res = numSqures(450);
    int a[3][3];
    printf("size: %u\n", sizeof(a));
    print_size(a);
    printf("minimu of squre number of %d is %d\n", 450, res);
}

void print_size(int a[][3]) {
    printf("sizeof a: %u a[0]:%u int: %u\n", (int) sizeof(*a), (int) sizeof(a[0]), (int) sizeof(int));
}
    

/**
 * recursive equition: num_squares(n) = min{num_squares((n - k)) + 1 ||　ｋ属于任意平方数}
 * @param n: n must less then INT_MAX.
 */
int numSqures(int n) {
    int max_squre_count = (int) sqrt(n);
    int *squre_list = (int *) malloc(max_squre_count * sizeof(int));
    for(int i=0;i<max_squre_count;i++) {
        squre_list[i] = pow(i+1, 2);
    }

    // 定义指针变量（数组）dp并初始化为最大值。
    int *dp = (int *) malloc((n+1) * sizeof(int));
    for(int i=1;i<=n;i++) {
        dp[i] = INT_MAX; // fill with max value of type int.
    }
    dp[0] = 0;

    for (int i=1;i<=n;i++) {
        for (int j=0;j<max_squre_count;j++) {
            if(i < squre_list[j]) {
                break;
            }
            dp[i] = (int) fmin(dp[i], dp[i - squre_list[j]] + 1);
        }
    }

    int result = dp[n];

    // 释放内存空间
    free(squre_list);
    squre_list = NULL;
    free(dp);
    dp = NULL;

    return result;
}