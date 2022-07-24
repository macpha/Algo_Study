#include <stdio.h>
#include <stdlib.h>

int fib(int n){
    if(n == 1 || n == 2)
        return 1;
    else
        return fib(n - 1) + fib(n - 2);
}

int fibonacci(int n){
    int* f = (int*)malloc(n * sizeof(int));
    f[0] = 0;
    f[1] = 0;
    int count = 0;
    
    for(int i = 2; i < n; i++){
        count++;
        f[i] = f[i - 1] + f[i - 2];
    }
    
    return count;
}

int main(){
    int n;
    scanf("%d", &n);
    
    printf("%d %d", fib(n), fibonacci(n));
}
