#include<stdio.h>



int main(){
    int prcs, burstTime, i,  prcs_no = 3;
    int burst_time[] = {5, 8, 12};
    int wt_time[10], tat[10];

    // wt_time[0] = 0;
    // wt time = burst time[i-1] + wt time[i-1]
    // tat = burst time[i] + wait time[i]

    wt_time[0] = 0;

    for (i = 1; i < prcs_no; i++)
        wt_time[i] = burst_time[i-1] + wt_time[i-1];

    for (i = 0; i < prcs_no; i++){
        tat[i] = burst_time[i] + wt_time[i];
        printf("%d\n", tat[i]);
    }
    

    printf("Turn Around times\tWaiting times\n");
    //for (int i = 0; i < prcs_no; i++)
     //   printf("%d\n", wt_time[i]);

    return 0;
}
