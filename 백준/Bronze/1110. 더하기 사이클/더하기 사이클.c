#include <stdio.h>

int main(){
    int n, count = 0;
    scanf("%d", &n);
    
    int d = n;
    while(1){
        int digit_n1 = d % 10, digit_n2 = d / 10;
        count++;
        
        int n2 = (digit_n1 * 10) + ((digit_n1 + digit_n2) % 10);
        d = n2;
        
        if(d == n)
            break;
    }
    
    printf("%d", count);
    
    return 0;
}
