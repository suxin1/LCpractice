#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>

int numSqures(int n);

int main() {
    int res = numSqures(9);
    printf("minimu of squre number of %d is %d", 9, res);
}


/**
 * recursive equition: num_squares(n) = min{num_squares((n - k)) + 1 ||　ｋ属于任意平方数}
 * @param n {int}: n * n must less then INT_MAX.
 */
int numSqures(int n) {
    printf("memory allocation start. \n");

    int max_squre_count = (int) sqrt(n);
    int *squre_list = (int *) malloc(max_squre_count * sizeof(int));
    for(int i=0;i<max_squre_count;i++) {
        squre_list[i] = pow(i+1, 2);
    }

    int *dp = (int *) malloc((n+1) * sizeof(int));
    for(int i=0;i<=n;i++) {
        dp[i] = INT_MAX; // full with max value of type int.
    }
    dp[0] = 0;

    printf("memory allocation done. %d \n", dp[n]);

    for (int i=1;i<=n;i++) {
        for (int j=0;j<max_squre_count;j++) {
            if(i < squre_list[j]) {
                break;
            }
            printf("num: %d, squre num: %d, index: %d \n.", n, squre_list[j], i);
            dp[i] = (int) fmin(dp[i], dp[i - squre_list[j]] + 1);
            
        }
    }

    printf("calculation done. \n");
    int result = dp[n];
    printf("free up memory. \n");
    free(squre_list);
    free(dp);
    return result;
}