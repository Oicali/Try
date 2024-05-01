#include<stdio.h>
#include"cs50.h"

int main (void){
    int n = 50;

    //This will print the memory address of the variable found in RAM.
    printf("%i \n\n", &n); 


    //This will print the memory address in HEXADECIMAL FORMAT of the variable found in RAM.
    printf("%p \n\n", &n); 


    //This will print the memory address in HEXADECIMAL FORMAT of the POINTER.
    //The * sign is used to access the value stored at the memory address to which the pointer points.
    int *p = &n;
    printf("%p \n\n", &p); 


    //This will now point out the value of integer 'n', using POINTERS, and print its value. 
    printf("%i \n", *p);


    //This print the memory address of a string
    string s = "HI!";

    for(int i = 0; s[i] != '\0'; i++){
        printf("%p \t", &s[i]);
    }
}