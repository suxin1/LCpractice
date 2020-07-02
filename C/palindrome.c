/**
 * 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
 * 说明：本题中，我们将空字符串定义为有效的回文串。
*/
#define true 1
#define false 0

#include <stdio.h>
#include <string.h>

typedef unsigned int bool;

bool isPalindrome(char *s);

bool validCharactor(char *c) {
    if((*c >= '0') && (*c <= '9')) return true;
    if((*c >='A') && (*c <= 'Z')) return true;
    if((*c >='a') && (*c <= 'z')) {
        *c = *c - ('a' - 'A');
        return true;
    }
    return false;
}

int main(void) {
    char str[] = "0P";
    printf("start function\n");
    bool res = isPalindrome(str);
    printf("result: %d\n", res);
    printf("stopped");
    return 0;
}

bool isPalindrome(char * s){
    int length = strlen(s);
    printf("string length: %d\n", length);
    int i = 0,j=length-1;
    while(i<j) {
        bool validHead = validCharactor(&s[i]);
        bool validTail = validCharactor(&s[j]);
        printf("%d:%d, %c:%c, %d:%d\n", validHead, validTail, s[i], s[j], i, j);
        if(!validHead) {
            i++;
            continue;
        }
        if(!validTail) {
            j--;
            continue;
        }
        if(s[i] != s[j]) return false;
        i++;
        j--;
    }
    return true;
}