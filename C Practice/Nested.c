#include <stdio.h>
#include "cs50.h"

int main (void){
    int x = get_int("How many: ");

    //Nested For loop creating a cube
    /*for (int i = 1; i<=x; i++){
        for(int j = 1; j<=x; j++){
            printf("* \t");
        }
    printf("\n");
    }*/

    //Nested for loop creating a slope
    /*for (int i = 1; i<=x; i++){
        for(int j = 1; j<=i; j++){
            printf("* \t");
        }
    printf("\n");
    }*/


    //Nested for loop creating a mirrored slope
    for (int i = 1; i<=x; i++){
        for(int j = x; j>=1; j--){
            if (j <= i) {
                printf("* \t");
            }

            else{
                printf("\t");
            }
            
        }
    printf("\n");
    }
}