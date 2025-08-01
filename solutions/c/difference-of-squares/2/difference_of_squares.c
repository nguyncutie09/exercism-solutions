#include "difference_of_squares.h"
#include <stdio.h>

unsigned int sum_of_squares(unsigned int number)
{
	unsigned int sumbp = 0;
	for(unsigned int i = 1; i <= number; i++)
	{
		sumbp += i*i;
	}
	return sumbp;
}
unsigned int square_of_sum(unsigned int number)
{
	unsigned int sum = 0;
	for(unsigned int j = 1; j <= number; j++)
	{
		sum += j; //dung ngoai vong lap
	}
	return sum*sum;
}
unsigned int difference_of_squares(unsigned int number)
{
	return (square_of_sum(number) - sum_of_squares(number));
}

