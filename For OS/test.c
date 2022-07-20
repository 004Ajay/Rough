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
    int reqArr[50], n, head, i, pos, dsk_sz, res=0, j, temp;
    printf("Enter number of requests: ");
    scanf("%d", &n);
    printf("Enter requests: ");
    for(i = 1; i <= n; i++)
        scanf("%d", &reqArr[i]);
    printf("Enter head position: ");
    scanf("%d", &head);
    printf("Enter total disk size: ");
    scanf("%d", &dsk_sz);
    reqArr[0] = head; // injecting head to first position of array
    reqArr[n+1] = dsk_sz; // injecting total disk size to array end
    
    for (i = 0; i <= n+1; i++)
    {
        printf("%d\t", reqArr[i]);
    }
    


}