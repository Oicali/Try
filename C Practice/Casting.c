#include<stdio.h>
#include"cs50.h"


int main (void){
    //Get the values from the users
    int x = get_int("x: ");
    int y = get_int("y: ");

    
    //divides the variables
    float z = (float) x / (float) y;   //Casted the int to float

    printf("The answer is: %f", z);

}