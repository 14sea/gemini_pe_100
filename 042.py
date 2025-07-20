"""
Project Euler Problem 42: Coded triangle numbers

Problem:
The n-th term of the sequence of triangle numbers is given by, t_n = (1/2)n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

Solution Idea:
1.  **Read and Parse the File**: First, we need to read the `words.txt` file. The file contains a single line of comma-separated, double-quoted words. We'll parse this line to get a clean list of words.

2.  **Generate Triangle Numbers**: We need a way to check if a word's value is a triangle number. Instead of checking for each word value individually, it's more efficient to pre-generate a set of triangle numbers up to a reasonable limit.
    - We need to estimate the maximum possible word value. The longest words in the file are around 14 characters. A word like "WWWWWWWWWWWWWW" would have a value of `14 * 23 = 322`. A word like "ZZZZZZZZZZZZZZ" would be `14 * 26 = 364`. Let's generate triangle numbers up to a value of 500 to be safe.

3.  **Calculate Word Values**: We'll loop through each word from the file. For each word, we calculate its value by summing the alphabetical positions of its letters (A=1, B=2, ...). The ASCII value of a character can be used for this: `ord(char) - ord('A') + 1`.

4.  **Check and Count**: For each calculated word value, we check if it exists in our pre-generated set of triangle numbers. If it does, we increment a counter.

5.  **Final Result**: The final value of the counter is the answer.
"""

def solve():
    """
    Finds the number of triangle words in the words.txt file.
    """
    try:
        with open('resources/documents/0042_words.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return "Error: words.txt not found. Please make sure the file is in the 'resources/documents/' directory."

    words = [word.strip('"') for word in content.split(',')]
    
    # Generate a set of triangle numbers up to a reasonable limit.
    # Max word length is ~14, max letter value is 26. Max value ~14*26 = 364.
    # Let's generate up to n=30, which gives t_30 = 465.
    triangle_numbers = {n * (n + 1) // 2 for n in range(1, 31)}
    
    triangle_word_count = 0
    for word in words:
        word_value = sum(ord(char) - ord('A') + 1 for char in word)
        if word_value in triangle_numbers:
            triangle_word_count += 1
            
    return triangle_word_count

if __name__ == "__main__":
    print(solve())
