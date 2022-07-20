#include <stdio.h>

int main(){
int i, j, pg_no, fr_no, ref_str[50], frame[10];

printf("\nEnter number of Pages: ");
scanf("%d", &pg_no);
printf("\nEnter number of Frames: ");
scanf("%d", &fr_no);

for(i = 0; i < fr_no; i++)
    frame[i] = -1;

printf("\nEnter Ref String: ");
for(i = 1; i <= pg_no; i++)
    scanf("%d", &ref_str[i]);









    return 0;
}
