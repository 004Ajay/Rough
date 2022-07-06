#include<stdio.h>

int max[100][100], alloc[100][100], need[100][100], avail[100];
int n, resrs, i, j;
void input();
void show();
void cal();

void input()
{
int i,j;
printf("Enter the no of Processes\t");
scanf("%d", &n);
printf("Enter the no of resources instances\t");
scanf("%d", &resrs);
printf("Enter the Max Matrix\n");
for(i=0;i<n;i++){
    for(j=0;j<resrs;j++){
scanf("%d",&max[i][j]);
}
}
printf("Enter the Allocation Matrix\n");
for(i=0;i<n;i++){
    for(j=0;j<resrs;j++){
scanf("%d",&alloc[i][j]);
}
}
printf("Enter the available Resources\n");
for(j=0;j<resrs;j++) {
scanf("%d",&avail[j]);
}
}


void show() {
int i,j;
printf("Process\tAllocation\tMax\tAvailable\t");
for(i=0;i<n;i++){
printf("\nP%d\t ",i+1);
for(j=0;j<resrs;j++) {
printf("%d ",alloc[i][j]); }
printf("\t");
for(j=0;j<resrs;j++) {
printf("%d ",max[i][j]); }
printf("\t");
if(i==0) {
for(j=0;j<resrs;j++)
printf("%d ",avail[j]);
}
}
}


void cal(){
int finish[100],temp,need[100][100],flag=1,k,c1=0;
int safe[100];
int i,j;
for(i=0;i<n;i++) {
finish[i]=0; }
//find need matrix
for(i=0;i<n;i++) {
for(j=0;j<resrs;j++) {
need[i][j]=max[i][j]
-alloc[i][j];
}}
printf("\n");
while(flag) {
flag=0;
for(i=0;i<n;i++) {
int c=0;
for(j=0;j<resrs;j++) {
if((finish[i]==0)&&(need[i][j]<=avail[j])) {
c++;
if(c==resrs) {
for(k=0;k<resrs;k++) {
avail[k]+=alloc[i][j];
finish[i]=1;
flag=1; }
printf("P%d->",i);
if(finish[i]==1){
i=n;
}}}}}}
for(i=0;i<n;i++) {
if(finish[i]==1) {
c1++;
}
else
{printf("P%d->",i);
}}
if(c1==n)
{printf("\nThe system is in safe state");
}
else{
printf("\nProcess are in dead lock");
printf("\nSystem is in unsafe state");
}
}





int main(){
printf("********** Banker's Algo ************\n");
input();
show();
cal();
return 0;
}


