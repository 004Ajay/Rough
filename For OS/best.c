#include<stdio.h>

int main(){
int  barray[20], parray[20], blk[20], prcs[20], i, j, blockNum, prcsNum, temp, lowest=9999;
printf("Memory Management - Best Fit\n");
printf("Enter the number of blocks:");
scanf("%d", &blockNum);
printf("\nEnter the number of processes:");
scanf("%d", &prcsNum);
printf("\nEnter the size of memory blocks:\n");
for(i = 1; i <= blockNum; i++){
    printf("Block no %d: ", i);
    scanf("%d",&blk[i]);
    }
printf("\nEnter the size of the processes :-\n");
for(i = 1; i <= prcsNum; i++){
    printf("Process no %d:",i);
    scanf("%d", &prcs[i]);
    }
for(i = 1; i <= prcsNum; i++){
    for(j = 1; j <= blockNum; j++){
if(barray[j] != 1){
temp = blk[j] - prcs[i];
if(temp >= 0)
if(lowest > temp){
parray[i]=j;
lowest=temp;
  }
 }
}
barray[parray[i]] = 1;
lowest=10000;
}
printf("\nProcess_no\tProcess_size\tBlock_no\tBlock_size");
for(i = 1; i <= prcsNum && parray[i] != 0; i++)
    printf("\n%d\t\t%d\t\t%d\t\t%d", i, prcs[i], parray[i], blk[parray[i]]);
return 0;
}