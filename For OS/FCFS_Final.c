#include<stdio.h>

int main(){
    int reqArr[20], n, start, i, pos, res=0, j, temp;
    printf("Enter number of requests: ");
    scanf("%d", &n);
    printf("Enter requests: ");
    for(i=0;i<n;i++)
        scanf("%d", &reqArr[i]);
    printf("Enter head position: ");
    scanf("%d", &start);
    //sorting
    for(i=0;i<n-1;i++) {
        for(j=0;j<n-1-i;j++) {
            if(reqArr[j]>reqArr[j+1]) {
                temp = reqArr[j];
                reqArr[j] = reqArr[j+1];
                reqArr[j+1] = temp;
            }
        }
    }
    /*
    // position of the disk to start seeking 
    for(i=0;i<n;i++) {                                      
        if(reqArr[i] == start) {
            pos = i;
            break;
        }
    }
    */
    res = abs(start - reqArr[0]);
    printf("%d -> %d", start, reqArr[1]);
    for(i = 0; i < n-1; i++){
        res += abs(reqArr[i+1] - reqArr[i]); 
        if(i == 1)
           continue;
        else
            printf(" -> %d", reqArr[i]);
    }
    printf("\nTotal Distance: %d\n", res);
    return 0;
}