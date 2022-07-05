#include<stdio.h>
#include<stdlib.h>
int mutex = 1, full = 0, empty = 3, x=0, n;

int wait(int s){
return(s--);
}
int signal(int s){
return(s++);
}
void producer(){
    mutex = wait(mutex);
    full = signal(full);
    empty = wait(empty);
    x++;
    printf("\nproducer produces the item%d",x);
    mutex = signal(mutex);
    }
void consumer(){
    mutex = wait(mutex);
    full = wait(full);
    empty = signal(empty);
    printf("\n consumer consumes item%d",x);
    x--;
    mutex = signal(mutex);
    }

int main(){
printf("\n1.PRODUCER\n2.CONSUMER\n3.EXIT\n");
while(1){
printf("\nChoice: \n");
scanf("%d",&n);
switch(n){ 
case 1: if((mutex == 1)&&(empty != 0))
        producer();
        else
        printf("Buffer is Full");
        break;

case 2: if((mutex == 1)&&(full != 0))
        consumer();
        else
        printf("Buffer is Empty");
        break;
case 3: exit(0);
default: printf("Choice exceeds limit.");
        }
    }
return 0;
}