def is_armstrong_number(number):
    n = len(str(number))
    result = 0
    for digit in str(number):
        result += int(digit) ** n
    return result == number