#include<stdio.h>



int main(){
    int prcs, prcs_no, burstTime;

    prcs_no = 3;

    int burst_time[] = {24, 3, 3};
    int wt_time[10];


    printf("Waiting times\n");
    wt_time[0] = 0;

    
    for (int i = 1; i < prcs_no; i++)
        wt_time[i] = burst_time[i+1];
    

    for (int i = 0; i < prcs_no; i++)
        printf("%d\n", wt_time[i]);

    return 0;
}
