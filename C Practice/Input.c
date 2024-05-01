#include<stdio.h>
#include"cs50.h"

int main (void){

    int x = get_int("Input first number: ");
    int y = get_int("Input second number: ");

    printf("%i\n", x + y);


    string name = get_string("What is your name: ");
    printf("Hello, %s", name);
}