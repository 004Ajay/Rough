#include <stdio.h>

int main() {
    int alloc[20], i, j, temp = 0;; 
    int blocks[] = {20, 50, 40, 30, 80};
    int prcs[] = {35, 45, 25};
    int blk_n = sizeof(blocks) / sizeof(blocks[0]);
    int prcs_n = sizeof(prcs) / sizeof(prcs[0]);
    
    for(i = 0; i < blk_n; i++){
        for(j = 0; j < blk_n-i-1; j++){
            if(blocks[j] < blocks[j+1]){
                temp = blocks[j];
                blocks[j] = blocks[j+1];
                blocks[j+1] = temp;
            }
        }
    }
    
    // for(i=0; i<blk_n; i++)
        
    
    for(i=0; i<blk_n; i++){
        alloc[i] = blocks[i];
        if(prcs[i] > blocks[i])
           blocks[i] = -1;
    }
    printf("\n\nBlocks Size\t\tProcess\t\t\tAllocated Blocks\n");
    for(j=0; j<blk_n; j++)
        printf("%d\t\t\t\t%d\t\t\t\t%d\n", alloc[j], prcs[j], blocks[j]);
    return 0;
}