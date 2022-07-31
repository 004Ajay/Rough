#include <stdio.h>

int i, j, temp = 0;

int sort(int arr[], int n){
    for(i = 0; i < n; i++){
        for(j = 0; j < n-i-1; j++){
            if(arr[j] < arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    
    int blocks[] = {10, 23, 21, 43, 65, 55, 47};
    int prcs[] = {1, 13, 11, 41, 63, 51, 37};
    int blk_n = sizeof(blocks) / sizeof(blocks[0]);
    int blk_n = sizeof(prcs) / sizeof(prcs[0]);
    
    sort(blocks, n);
    
    for(i=0; i<7; i++){
    printf("blocks [%d] : %d\n", i+1, blocks[i]);
    }
    return 0;
}