/** 
 * 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
 */
#define true 1
#define false 0

#include <stdio.h>
#include <string.h>

#define VOWELS "aeiouAEIOU"

typedef unsigned int bool;


char* reverseVowels(char *s);
bool isVowel(char s);

int main(void) {
    char *s = "hello";
    printf("start\n");
    reverseVowels(s);
    printf("result: %s", s);
}

bool isVowel(char s) {
    char * r = strchr(VOWELS, s);
    return r?true:false;
}

char * reverseVowels(char * s) {
    int length = strlen(s);
    printf("length of sentence: %d\n", length);
    
    int i=0, j=length-1;
    char temp;
    while(i<j) {
        bool headIsVowel = isVowel(s[i]);
        bool tailIsVowel = isVowel(s[j]);
        if(!headIsVowel) {
            i++;
            continue;
        }
        if(!tailIsVowel) {
            j--;
            continue;
        }
        // swapCharactor(&s[i], &s[j]);
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;

        i++;
        j--;
    }
    return s;
}