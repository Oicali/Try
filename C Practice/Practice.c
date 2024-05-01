#include <stdio.h>                       //Header file => This file lets user to input and output

int main(void){                          //Event syntax similar to when green flag is clicked in Scratch
    int age;
    char name[100];                     //initialization for string 
                        

    printf("Type your name: ");
    scanf("%[^\n]s", name);              // %[^\n]s => tells scanf to read everything until newline and store it in name variable. 
    printf("Welcome, %s!", name);        //%s => plug in some value for string


    printf("\nEnter your age: ");
    scanf("%d", &age);                   // %d => plug in some value for int
    printf("You are %d years old\n", age); 

        /*
        bool                            => 2 bytes or 16 bits
        char    => get_char     => %c   => 1 byte or 8 bits 
        double  => get_double           => 8 bytes or 64 bits 
        float   => get_float    => %f   => 4 bytes or 32 bits
        int     => get_int      => %i   => 4 bytes or 32 bits
        long    => get_long     => %li  => 4 bytes or 32 bits
        string  => get_string   => %s
        */


    
}