import time
import random
import math
"""
    Example function to show how to print results out.
"""
def test_case_example(input_number):
    # Checks if the number if divisible by 5
    if (input_number % 5) == 0:
        print("\tIs divisible by 5")
    else:
        print("\tIs not divisible by 5")

"""
    May use this function to generate extra test files
"""
def generate_random_test_file():
    file_name = time.strftime("%Y_%m_%d_%H_%M_%S") + '.txt'
    number_of_test_cases = 50

    with open(file_name, 'w') as test_file:
        for _ in range(number_of_test_cases):
            # Print random number from 1 to 100
            test_file.write(str(random.randint(1,100)) + "\n")

def main():
    input_file_name = 'input_file.txt'
    input_file = open(input_file_name, 'r')

    for input_number in input_file.readlines():
        current_number = int(input_number.strip())
        print("Current number %d:" % (current_number))
        #test_case_example(current_number)

        # Add your functions below here
        
        if (current_number > 26):
            n=(current_number/26)
            if (n == 2) or (n == 3):
                n=math.trunc(n)
                letter=chr(current_number-((n-1)*26) +96)
                print(letter)
            else:
                n=math.trunc(current_number/26)
                letter=chr(current_number-(n*26) +96)
                print(letter)
        else:
            letter=chr(current_number +96)
            print(letter)



        print("-----------------------------------------------------")



if __name__ == "__main__":
    main()
