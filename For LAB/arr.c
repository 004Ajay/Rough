#include<stdio.h>

int main(){
    int arr[] = {2, 5, 3, 4, 6};
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("%d\n", n);
    int sum = 0;

    for (int i = 0; i < n; i++){
        sum += arr[i];
    }
    printf("total: %d\n", sum);
    printf("average: %d", sum/n);
    return 0;
}
