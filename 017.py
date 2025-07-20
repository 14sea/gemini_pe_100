def solve():
    """
    Solves the Project Euler Problem 17.

    Question:
    If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out
    in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
    and forty-two) contains 23 letters and 115 (one hundred and fifteen)
    contains 20 letters. The use of "and" when writing out numbers is in
    compliance with British usage.

    Solution Idea:
    The core of the solution is a function that converts a number into its
    English word representation. We can pre-define the word forms for units (1-9),
    teens (10-19), and tens (20, 30,...).

    The function will handle numbers by breaking them down:
    - For numbers < 20, we use the direct mapping.
    - For numbers < 100, we combine a 'tens' word with a 'units' word.
    - For numbers < 1000, we use the 'hundreds' digit, add "hundred", and if
      there's a remainder, we add "and" and recursively process the remainder.
    - 1000 is a special case, "one thousand".

    We then loop from 1 to 1000, convert each number to words, strip out
    spaces and hyphens, and sum the lengths of the resulting strings.
    """
    units = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 0: ""
    }
    teens = {
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }

    def number_to_words(n):
        if 1 <= n < 10:
            return units[n]
        if 10 <= n < 20:
            return teens[n]
        if 20 <= n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else units[n % 10])
        if 100 <= n < 1000:
            return units[n // 100] + "hundred" + ("" if n % 100 == 0 else "and" + number_to_words(n % 100))
        if n == 1000:
            return "onethousand"
        return ""

    total_letters = 0
    for i in range(1, 1001):
        words = number_to_words(i)
        total_letters += len(words)
        
    print(f"The total number of letters used is: {total_letters}")

solve()