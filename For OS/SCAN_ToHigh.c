#include<stdio.h>

int main(){
    int req[30], i, j, n, dist=0, head, size, move=1; //moves to low values
    printf("Enter number of requests: ");
    scanf("%d",&n);
    printf("Enter requests: ");
    for(i = 0; i < n; i++)
     scanf("%d",&req[i]);
    printf("Enter head position: ");
    scanf("%d",&head);
    printf("Enter total disk size: ");
    scanf("%d",&size);
    // Sorting using bubble sort (short job first)
    for(i=0;i<n;i++){
        for(j=0;j<n-i-1;j++){
            if(req[j]>req[j+1]){
                int temp;
                temp=req[j];
                req[j]=req[j+1];
                req[j+1]=temp;
            }
        }
    }
    int index;
    for(i=0;i<n;i++){
        if(head<req[i]){
            index=i;
            break;
        }
    }
    // if movement is towards high value
    if(move == 1){
        for(i = index; i < n; i++){
            dist = dist + abs(req[i] - head);
            head = req[i];
        }
        //  last movement for max size 
        dist = dist + abs(size - req[i-1]-1);
        head = size - 1;
        for(i = index - 1; i >= 0; i--){
             dist = dist + abs(req[i] - head);
             head = req[i];
        }
    }
    printf("Total Distance: %d", dist);
    return 0;
}