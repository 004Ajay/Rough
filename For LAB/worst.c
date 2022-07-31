#include<stdio.h>
#define max 25

void main(){
int block_sz[max], prcs_sz[max], bf[max],ff[max], i, j, num_of_blocks, num_of_prcs, temp, highest=0;
printf("\nMemory Management Scheme - Worst Fit\n");
printf("\nEnter number of blocks: ");
scanf("%d",&num_of_blocks);
printf("Enter size of blocks:\n");
for(i = 1; i <= num_of_blocks; i++){
 printf("Block %d: ", i);
 scanf("%d",&block_sz[i]);
}

printf("Enter number of Processes: ");
scanf("%d",&num_of_prcs);
printf("Enter size of Processes:\n");
for(i=1;i<=num_of_prcs;i++){
 printf("Process %d: ", i);
 scanf("%d", &prcs_sz[i]);
}

for(i=1;i<=num_of_prcs;i++){
	for(j=1;j<=num_of_blocks;j++){
		if(bf[j]!=1){
			temp = block_sz[j] - prcs_sz[i];
			if(highest < temp){
				ff[i] = j;
				highest = temp;
			}
		}
	}
	bf[ff[i]] = 1;
	highest = 0;
}

printf("\nProcess No  \tProcess Size  \tBlocks");
for(i = 1; i <= num_of_prcs; i++)
    printf("\n%d\t\t%d\t\t%d", i-1, prcs_sz[i], block_sz[ff[i]]);
printf("\n");
}