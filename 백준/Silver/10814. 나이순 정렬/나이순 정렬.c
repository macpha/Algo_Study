#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct client{
    int age;
    char name[101];
}info;

int compare(const void* w1, const void* w2){
    info* client1 = (info*)w1;
    info* client2 = (info*)w2;
    
    if(client1->age > client2->age)
        return 1;
    else if(client1->age < client2->age)
        return -1;
    else
        return 0;
}

int main(){
    int N;
    scanf("%d", &N);
    
    info* arr = (info*)malloc(N * sizeof(info));
    for(int i = 0; i < N; i++)
        scanf("%d %s", &(arr + i)->age, (arr + i)->name);
    
    qsort(arr, N, sizeof(arr[0]), compare);
    for(int i = 0; i < N; i++)
        printf("%d %s\n", (arr + i)->age, (arr + i)->name);
    
    return 0;
}
