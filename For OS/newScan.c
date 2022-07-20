#include<stdio.h>

int main(){
    int diskQueue[20], n, start, i, pos, diff, seekTime=0, current, j, tmp;
    printf("Enter size of Queue: ");
    scanf("%d", &n);
    printf("Enter Queue: ");
    for(i=1;i<=n;i++)
        scanf("%d", &diskQueue[i]);
    printf("Enter head position: ");
    scanf("%d", &start);
    diskQueue[0] = start; // injecting to the first position
    ++n;
    // sorting
    for(i=0;i<n-1;i++) {
        for(j=0;j<n-1-i;j++) {
            if(diskQueue[j]>diskQueue[j+1]) {
                tmp = diskQueue[j];
                diskQueue[j] = diskQueue[j+1];
                diskQueue[j+1] = tmp;
            }
        }
    }
    // position of the disk to start seeking 
    for(i=0;i<n;i++) {                                      
        if(diskQueue[i] == start) {
            pos = i;
            break;
        }
    }
    // start seeking to the right
    for(i=pos;i<n-1;i++) {
        diff = abs(diskQueue[i+1] - diskQueue[i]);
        seekTime += diff;
    }
    printf("\nTotal Distance: %d\n", seekTime);
    return 0;
}