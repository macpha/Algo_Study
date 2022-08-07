#include <stdio.h>
#include <stdlib.h>

int main(){
    int chess[6] = {1, 1, 2, 2, 2, 8};
    int search;
    
    for(int i = 0; i < 6; i++){
        scanf("%d", &search);
        printf("%d ", chess[i] - search);
    }
    
    return 0;
}
