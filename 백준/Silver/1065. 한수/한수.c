#include <stdio.h>

int hannum(int n){
    int digit_n[5], cnt = 0;
    
    while(n != 0){
        digit_n[cnt] = n % 10;
        n /= 10;
        cnt++;
    }
    
    int seq = 10;
    for(int i = 0; i < cnt - 1; i++){
        int d = digit_n[i + 1] - digit_n[i];
        if(seq == 10)
            seq = d;
        if(seq != d)
            return 0;
    }
    
    return 1;
}

int count_han(int n){
    int count = 0;
    
    for(int i = 1; i < n + 1; i++)
        if(hannum(i) == 1)
            count++;
    
    return count;
}

int main(){
    int n;
    scanf("%d", &n);
    
    printf("%d", count_han(n));
}
