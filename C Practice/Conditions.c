#include <stdio.h>
#include"cs50.h"

int main (void){
    int x = get_int ("X: ");
    int y = get_int ("Y: ");

    if (x > y ) {
        printf("%i is greater than %i", x, y);
    }
    else if (x < y) {
        printf("%i is less than %i", x, y);
    }
    else {
        printf("%i and %i are equal", x, y);

    }

    string s = get_string("\ns: "); 
    string t = get_string("t: ");

    //Not the same when s and t are typed the same
    //This is why we use str.cmp 
    if(s == t){
        printf("%p \n", &s);
        printf("%p \n", &t);
        printf("s and t are same\n");
    } else {
        printf("%p \n", &s);
        printf("%p \n", &t);
        printf("s and t are different\n");
    }

    //For some reason it is the same
    //This actually works, probably because the pointing to the address of the "Hi"
    string i = "Hi";  
    string j = "Hi";

    if(i == j){
        //the address of pointers(?) are the same
        //must be because you are comparing the address of the pointers
        printf("%p \n", i);
        printf("%p \n", j);

        printf("%p \n", &i);
        printf("%p \n", &j);
        printf("i and j are SAME\n");
    } else {
        //the address of pointers(?) are not the same
        printf("%p \n", i);
        printf("%p \n", j);

        printf("%p \n", &i);
        printf("%p \n", &j);
        printf("i and j are not same\n");
    }

}