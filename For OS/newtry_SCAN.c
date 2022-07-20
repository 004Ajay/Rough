#include<stdio.h>

int main(){
    int diskQueue[20], n, start, i, pos, diff=0, j, temp;
    printf("Enter size of Queue: ");
    scanf("%d", &n);
    printf("Enter Queue: ");
    for(i=0;i<n;i++)
        scanf("%d", &diskQueue[i]);
    printf("Enter head position: ");
    scanf("%d", &start);
    //sorting
    for(i=0;i<n-1;i++) {
        for(j=0;j<n-1-i;j++) {
            if(diskQueue[j]>diskQueue[j+1]) {
                temp = diskQueue[j];
                diskQueue[j] = diskQueue[j+1];
                diskQueue[j+1] = temp;
            }
        }
    }
    for(i=0; i<n;i++)
        printf("%d\t", diskQueue[i]);
    // position of the disk to start seeking 
    for(i=0;i<n;i++) {                                      
        if(diskQueue[i] == start) {
            pos = i;
            break;
        }
    }
    diff = abs(start - diskQueue[1]);
    printf("\n");
    printf("%d -> %d", start, diskQueue[1]);
    for(i = 0; i < n; i++){
        
        if(i == 1) {
            diff += abs(diskQueue[i+1] - diskQueue[i]);
            continue;
        }
        else{
            printf(" -> %d", diskQueue[i]);

        }
        

    
    }
    printf("\nTotal Distance: %d\n", diff);
    return 0;
}