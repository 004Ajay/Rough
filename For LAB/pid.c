#include<stdio.h>
#include<sys/types.h>
// #include<stdlib.h>
// #include<sys/wait.h>
#include<unistd.h>

int main(){
    printf("Your process id: %d", getpid());

    if (fork() != 0)
        printf("Success");
    else
    printf("No Success");    


    return 0;
}
