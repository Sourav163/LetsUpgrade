// Write a C program that contains a function called reverseString which takes a string as input and reverses it. The program should also include a main function that prompts the user to enter a string, calls the reverseString function to reverse the string, and then displays the reversed string.

#include <stdio.h>
#include <conio.h>
#include <string.h>

void reverseString(char *str)
{
    int len = strlen(str);
    int i, j;
    char temp;

    for (i = 0, j = len - 1; i < j; i++, j--)
    {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

int main()
{
    char str[100];

    // User Input :
    printf("Enter a string :  ");
    fgets(str, 100, stdin);

    // Remove the newline character from the input :
    str[strcspn(str, "\n")] = '\0';

    reverseString(str);

    printf("The reversed string is :  %s", str);

    return 0;
}
