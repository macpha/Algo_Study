#include <stdio.h>
#include <stdlib.h>

int main(){
    unsigned int X, N, a, b, sum = 0;
    
    
    scanf("%u\n%u", &X, &N);
    for(int i = 0; i < N; i++){
        scanf("%u %u", &a, &b);
        sum += a * b;
    }
    
    if(sum == X)
        printf("Yes");
    else
        printf("No");
    
    return 0;
}
