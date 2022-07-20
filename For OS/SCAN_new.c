/*
For SCAN (example)
Number of request: 9
Request Order: 86 1470 913 1774 948 1509 1022 1750 130
Head Position: 143
Required Disance: 1745 (as per classwork)

Total disk size: 4999 (if)
*/

#include<stdio.h>

int main(){
    int reqArr[20], n, head, i, pos, dsk_sz, res=0, j, temp;
    printf("Enter number of requests: ");
    scanf("%d", &n);
    printf("Enter requests: ");
    for(i=0;i<n;i++)
        scanf("%d", &reqArr[i]);
    printf("Enter head position: ");
    scanf("%d", &head);
    printf("Enter total disk size: ");
    scanf("%d", &dsk_sz);
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
    // position of the disk to head seeking 
    for(i=0;i<n;i++) {                                      
        if(reqArr[i] == head) {
            pos = i;
            break;
        }
    }
    */
    res = abs(head - reqArr[0]);
    printf("%d -> %d", head, reqArr[1]);
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