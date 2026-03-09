#include<stdio.h>
#include<stdlib.h>
#include<time.h>
// guessing game 
int num , inp , i;



//fuction to generate random number
int gennum(){
    srand(time(NULL));
    num = (rand()%100);
    return num;
}

int main(){
   
    printf("WELCOME TO THE NUMBER GUESSING GAME\n");
    printf("YOU HAVE 5 ATTEMPTS TO GUESS THE NUMBER\n");
   
 //calling the function to generate random number 

      gennum();

for (i = 0; i < 5; i++){
    //taking input from user
     printf("ENTER A NUMBER BETWEEN 1 TO 100:\n");
    scanf("%d",&inp);
    
       // coditions of game

    if( num==inp){
        printf("YOU WIN THE GAME \n");
        break;
    }
    else if (num>inp)
    {
        printf("NUMBER IS high\n");

    }
    else if (num<inp)
    {
        printf("NUMBER IS low\n");
    }
    else if(num<0)
    {
        printf("NEGATIVE NUMBER\n");
    }
    else if(num>=100 || num<=0)
    {
        printf("OUT OF BOUND\n");
    }
   
}
if (num!=inp || i==5){
    printf("YOU LOSE THE GAME \n");
}
printf("THE NUMBER WAS %d\n",num);

   
    return 0 ;
}