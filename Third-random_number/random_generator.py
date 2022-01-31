
'''
Really simplified random number generator made only for Docker course purposes

Author: Marcin Dyrdół
'''

import sys
from random import randint
from tokenize import String
from typing import Any

EXIT_CODE = -1

def is_int(element : Any) -> bool:
    try:
        int(element)
        return True
    except ValueError:
        return False

def processInput( min : str, max : str) -> tuple:
    if(is_int(min) and is_int(max)):
        min_number = int(min)
        max_number = int(max)
        return min_number,max_number
    return EXIT_CODE,EXIT_CODE

def numberPicker( number_range : tuple) -> None:
    min,max = number_range
    if(max<=min):
        print("Invalid input - shutting down..")
        sys.exit(EXIT_CODE)
    
    rand_num = randint(min,max)
    print(rand_num)
    

def main() -> None:
    
    min_number : str = input('Please enter the min number: ')
    max_number : str = input('Please enter the max number:')
    number_range_tuple = processInput(min_number,max_number)
    numberPicker(number_range_tuple)
    
if __name__ == '__main__':
    main()