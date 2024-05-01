#include<stdio.h>
#include<string.h> 
#include"cs50.h"

int main (void) {
    int scores[3];

    scores[0] = 90;
    scores[1] = 93;
    scores[2] = 94;


    string s = get_string("INPUT: ");
    printf("OUTPUT: ");

    for(int i=0 ; i < strlen(s); i++) {  //strlen()is from the library <string.h> || You could also use s[i] != \0 to indicated the end of the string
        printf("%i ", s[i]);                //Since %i was used, it converts every char from the string into numerical value based from the ASCII
    }

}
