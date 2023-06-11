// Write a program in C that takes an input number from the user and determines whether it is even or odd. If the number is even, the program should display the message "Number is even." If the number is odd, the program should display the message "Number is odd."

#include<stdio.h>
int main () {
    int num;

    // Sample:
    // num = 15;

    // User Input :
    printf("Enter The Number :  ");
    scanf("%d", &num);

    if(num%2 == 0) {
        printf("Number is even.");
    }
    else{
        printf("Number is odd.");
    }
}