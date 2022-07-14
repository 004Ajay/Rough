#include <stdio.h>
int main(){
int b[20], f[20], bno, fno, i, j, temp, barr[20], farr[20];
printf("\nMemory Management Scheme - Best Fit");
printf("\nEnter number of blocks: ");
scanf("%d", &bno);
int lowest = 9999;
printf("Enter size of blocks\n");
for (i = 1; i <= bno; i++)
{printf("Block no.%d: ", i);
scanf("%d", &b[i]);
}
printf("\nEnter number of files: ");
scanf("%d", &fno);
printf("Enter size of files\n");
for (i = 1; i <= fno; i++)
{
printf("File no.%d: ", i);
scanf("%d", &f[i]);
}
for (i = 1; i <= fno; i++)
{
for (j = 1; j <= bno; j++)
{
if (barr[j] != 1){
temp = b[j] - f[i];
if (temp >= 0)
if (lowest > temp){
farr[i] = j;
lowest = temp;
}
}
}
barr[farr[i]] = 1;
lowest = 10000;
}
printf("\nFile_no\t\tFile_size\tBlock_no\tBlock_size");
for (i = 1; i <= fno && farr[i] != 0; i++){
     printf("\n%d\t\t%d\t\t%d\t\t%d", i, f[i], farr[i], b[farr[i]]);
}
printf("\n");
}

