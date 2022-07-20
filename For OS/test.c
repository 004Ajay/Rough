/* 
    Author     : abhijithvijayan
    Created on : 04 Nov 18, 20:15
    Title      : SCAN Disk Scheduling
*/

#include<stdio.h>
#include<stdlib.h>

void scan(int Ar[20], int n, int start);
void sort(int Ar[20], int n);

int main() {
    int diskQueue[20], n, start, i;
    printf("Enter the size of Queue: ");
    scanf("%d", &n);
    printf("Enter the Queue: ");
    for(i=1;i<=n;i++) {                                     /* head element to be read */ 
        scanf("%d",&diskQueue[i]);
    }
    printf("Enter the initial head position: ");
    scanf("%d", &start);                                
    diskQueue[0] = start;                                    /* injecting to the first position */
    ++n;
    sort(diskQueue, n);                                     /* total of n+1 elements */    
    scan(diskQueue, n, start);

    return 0;
}

void scan(int Ar[20], int n, int start) {
    int i, pos, diff, seekTime=0, current;
    // position of the disk to start seeking 
    for(i=0;i<n;i++) {                                      
        if(Ar[i]==start) {
            pos=i;
            break;
        }
    }
    // start seeking to the right
    printf("\nMovement of Cylinders\n");
    for(i=pos;i<n-1;i++) {
        diff = abs(Ar[i+1] - Ar[i]);
        seekTime += diff;
        printf("Move from %d to %d with seek time %d\n", Ar[i], Ar[i+1], diff);
    }
    current=i;                                              /* last element position */
    // start seeking to the left
    for(i=pos-1;i>=0;i--) {
        diff = abs(Ar[current] - Ar[i]);
        seekTime += diff;
        printf("Move from %d to %d with seek time %d\n", Ar[current], Ar[i], diff);
        current=i;
    }
    printf("\nTotal Seek Time: %d", seekTime);
    // average of entered elements(n-1) excluding head
    printf("\nAverage Seek Time = %f",(float) seekTime/(n-1));
    printf("\n");
}

void sort(int Ar[20], int n) {
    int i, j, tmp;
    for(i=0;i<n-1;i++) {
        for(j=0;j<n-1-i;j++) {
            if(Ar[j]>Ar[j+1]) {
                tmp = Ar[j];
                Ar[j] = Ar[j+1];
                Ar[j+1] = tmp;
            }
        }
    }
}

/* OUTPUT

    Enter the size of Queue: 5
    Enter the Queue: 100 50 10 20 75
    Enter the initial head position: 35

    Movement of Cylinders
    Move from 35 to 50 with seek time 15
    Move from 50 to 75 with seek time 25
    Move from 75 to 100 with seek time 25
    Move from 100 to 20 with seek time 80
    Move from 20 to 10 with seek time 10

    Total Seek Time: 155
    Average Seek Time = 31.000000
    
*/