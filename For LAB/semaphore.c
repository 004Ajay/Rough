#include<stdio.h>

int mutex = 1, full = 0, empty = 3, item = 0;

int wait(int s){
    return (--s);
}

int signal(int s){
    return (++s);
}

void prod(){
    //mfeipm
    mutex = wait(mutex);
    full = signal(full);
    empty = wait(empty);
    item++;
    printf("Producer produces items\n");
    mutex = signal(mutex);
}

void cons(){
    //mfepim
    mutex = wait(mutex);
    full = wait(full);
    empty = signal(empty);
    printf("Consumer consumes items\n");
    item--;
    mutex = signal(mutex);

}


int main(){

    int choice;
    printf("1: Producer\n2: Consumer\n");
    while (1){
    printf("Choice: ");
    scanf("%d", &choice);
    switch(choice){

        case 1: if(mutex == 1 && empty != 0)
                prod();
                else
                printf("Buffer is full");
                break;

        case 2: if(mutex == 1 && full != 0)
                cons();
                else
                printf("Buffer is empty");
                break;
        // case 3: exit code        
    }
    }
    return 0;
  
}
