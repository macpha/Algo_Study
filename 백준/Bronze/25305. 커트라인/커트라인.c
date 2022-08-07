#include <stdio.h>
#include <stdlib.h>

int compare(const void* s1, const void* s2){
    int num1 = *(int*)s1;
    int num2 = *(int*)s2;
    
    if(num1 < num2)
        return 1;
    
    else if(num1 > num2)
        return -1;
    
    else
        return 0;
}

int main(){
    int N, k;
    
    scanf("%d %d", &N, &k);
    
    int score[N];
    for(int i = 0; i < N; i++)
        scanf("%d", &score[i]);
    
    qsort(score, N, sizeof(score[0]), compare);
    
    printf("%d", score[k - 1]);
    
    return 0;
}
