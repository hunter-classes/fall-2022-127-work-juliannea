//Extra done is showed a working function 
//Extra done is showed a working if and for loop 

#include <iostream>
#include <string>
#include <stdio.h>

//creating function 

int summation(int number)
{
  int summation = 1;
  for(int i = number; i > 1; i--) //for loop 
  {
    summation += i;  
  }
  return summation;
}

int main() 
{
  std::cout << "Hello World!\n";
  std::cout << " \n";

  int age1 = 6;
  int age2 = 8;

  if(age1 < age2) //if statement 
  {
    std::cout<<"age 1: "<< age1 << " is greater than age 2: "<< age2 << std::endl;

    int sum = summation(age1);
    printf("%d is the summation of age 1: 6", sum);
  }
  else
  {
    std::cout<<"age 2: "<< age2 << " is greater than age 1: "<< age1 << std::endl;

    int sum = summation(age2);
    printf("%d is the summation of age 2", sum);
  }
}