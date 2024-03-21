#!/usr/bin/python3
def roman_to_int(roman_string):

    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'L': 50,
            'D': 500,
            'M': 1000
            }
    sum = 0

    if (not roman_string or not isinstance(roman_string, str)):
        return (0)
    len_str = len(roman_string)

    for num in range(len_str):

        if roman.get(roman_string[num], 0) == 0:
            return (0)

        n = roman[roman_string[num]]

        if num != len_str - 1 and n < roman[roman_string[num + 1]]:
            sum += roman[roman_string[num]] * -1

        else:
            sum += roman[roman_string[num]]

    return sum
