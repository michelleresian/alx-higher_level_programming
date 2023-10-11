#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 100
    }

    curr_value = 0
    pre_value = 0

    for c in reversed(roman_string):
        value = roman_string.get(c, 0)
        if value >= pre_value:
            curr_value += value
        else:
            curr_value -= value
        pre_value = value

    return curr_value
