#include <stdio.h>

int sorted_arr[1000001];

void merge(int* arr, int left, int mid, int right){
    int i = left, j = mid + 1, k = left;
    
    while(i <= mid && j <= right){
        if(arr[i] < arr[j])
            sorted_arr[k++] = arr[i++];
        else
            sorted_arr[k++] = arr[j++];
    }
    
    if(i <= mid)
        for(int l = i; l <= mid; l++)
            sorted_arr[k++] = arr[l];
    
    else
        for(int l = j; l <= right; l++)
            sorted_arr[k++] = arr[l];
    
    for(int l = left; l <= right; l++)
        arr[l] = sorted_arr[l];
}

void merge_sort(int* arr, int left, int right){
    if(left < right){
        int mid = (left + right) / 2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main(){
    int N;
    scanf("%d", &N);
    
    int arr[N];
    for(int i = 0; i < N; i++)
        scanf("%d", &arr[i]);
    
    merge_sort(arr, 0, N - 1);
    
    for(int i = 0; i < N; i++)
        printf("%d\n", arr[i]);
    
    return 0;
}
