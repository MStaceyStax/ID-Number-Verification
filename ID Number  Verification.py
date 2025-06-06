# ID Number Verification
# This program verifies the validity of an ID number based on the Luhn alogorithm.
# It checks if the ID number is 13 digits Long, characters are digits and if the ID number is valid.

# The luhn alogorithm is a simple checksum formula used to validate a variety of identification numbers, such as a credit card number, IMEI number, National ID number, etc.

# The algorithim works as follows:
# 1. Starting from the rightmost digit, double the value of every second digit. If the result is greater than 9, subtract 9 from it.
# Index: 12 11 10 9 8 7 6 5 4 3 2 1 0
# 2. Sum all the digits.
#Digit: 8  8  0  4  0  7  0  1  5  1  0  8  6
# Sum = 8 + 7 + 0 + 8 + 0 + 5 + 0 + 2 + 5 + 2 + 0 + 7 + 6 = 50
# 50 % 10 = 0
# The sum modulo 10 is equal to 0, so the number is valid.
# 3. If the total modulo 10 is equal to 0, then the number is valid.
# 4. If the total modulo 10 is not equal to 0, then the number is invalid.
# 5. The ID number must be 13 digits long.
# 6. The ID number must contain only digits.


# Example usage of the function

def ValidateSAID(id): 
    # Check if the ID number is 13 digits long
    if len(id) != 13:
        return False
    # Check if the ID number contains only digits
    if not id.isdigit():
        return False
    # Convert the ID number to a list of digits
    digits = [int(d) for d in id]
    # Double every second digit from the right
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        # If the result is greater than 9, subtract 9 from it
        if digits[i] > 9:
            digits[i] -= 9
    # Calculate the sum of all the digits
    total = sum(digits)
    # Check if the total modulo 10 is equal to 0
    return total % 10 == 0

SAid = input("Enter your ID number: ")
if ValidateSAID(SAid):  
    print("Valid SAID number")
else:
    print("Invalid SAID number")



# The program will prompt the user to enter an ID number and check if it is valid according to the Luhn algorithm.