"""
Project Euler Problem 89: Roman numerals

Problem:
The file roman.txt contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals. Find the number of characters saved by writing each of these in their minimal form.

Solution Idea:
The process is to convert each Roman numeral to its integer value, then convert that integer back into its most efficient (minimal) Roman numeral representation. The total saving is the difference in string lengths.

1.  **Roman to Integer**: A function `roman_to_int` will parse the Roman numeral string. It handles subtractive notation (like IV, IX) by checking if a smaller value numeral precedes a larger one.

2.  **Integer to Minimal Roman**: A function `int_to_roman` will convert an integer to its minimal Roman form. This is done greedily by using a descending list of values and their corresponding numerals (including subtractive forms like 900 for 'CM', 400 for 'CD', etc.).

3.  **Main Logic**:
    - Read each line from the file.
    - For each Roman numeral, record its original length.
    - Convert it to an integer.
    - Convert the integer back to a minimal Roman numeral.
    - Record the new length.
    - Add the difference `(original_length - new_length)` to a running total.
    - The final total is the answer.
"""

def roman_to_int(s):
    """Converts a Roman numeral string to an integer."""
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(s):
        # Check for subtractive notation
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            total += roman_map[s[i+1]] - roman_map[s[i]]
            i += 2
        else:
            total += roman_map[s[i]]
            i += 1
    return total

def int_to_roman(n):
    """Converts an integer to its minimal Roman numeral representation."""
    val_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    roman_str = ""
    for val, numeral in val_map:
        # Append the numeral as many times as its value fits into n
        count, n = divmod(n, val)
        roman_str += numeral * count
    return roman_str

def solve():
    """
    Calculates the number of characters saved by writing each Roman numeral
    in the file in its minimal form.
    """
    try:
        with open('resources/documents/0089_roman.txt', 'r') as f:
            roman_numerals = [line.strip() for line in f]
    except FileNotFoundError:
        return "Error: roman.txt not found. Please ensure it's in 'resources/documents/'."

    total_chars_saved = 0
    for numeral in roman_numerals:
        original_len = len(numeral)
        
        number = roman_to_int(numeral)
        minimal_numeral = int_to_roman(number)
        minimal_len = len(minimal_numeral)
        
        total_chars_saved += (original_len - minimal_len)
        
    return total_chars_saved

if __name__ == "__main__":
    print(solve())
