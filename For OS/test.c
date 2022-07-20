#include <stdio.h>

int main() {
    int i=0, diff = 0;
    int arr[9] = {86, 130, 913, 948, 1022, 1470, 1509, 1750, 1774};
    while(i < 8){
        diff += (arr[i+1] - arr[i]);
        printf("%d - %d = %d\n", arr[i+1], arr[i], arr[i+1] - arr[i]);
        //printf("%d\t", diff);
        i++;
    }
    
    
    printf("\nsum: %d", diff+128);    
    
    return 0;
}