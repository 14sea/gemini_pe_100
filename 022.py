"""
Project Euler Problem 22: Names scores

Problem:
Using names.txt (a 46K text file containing over five-thousand first names), begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

Solution Idea:
1. Read the names from the file. The names are in a single line, separated by commas, and each name is enclosed in double quotes.
2. Parse the string to get a list of individual names. We'll need to remove the quotes from each name.
3. Sort the list of names alphabetically.
4. Initialize a total score variable to 0.
5. Iterate through the sorted list of names, keeping track of the position of each name (starting from 1).
6. For each name, calculate its alphabetical value. This is the sum of the alphabetical positions of its letters (A=1, B=2, ..., Z=26). We can get this by taking the ASCII value of each letter and subtracting the ASCII value of 'A', then adding 1.
7. Multiply the alphabetical value by the name's position in the list to get the name score.
8. Add this name score to the total score.
9. After iterating through all the names, the total score will be the answer.
"""

def solve():
    """
    Calculates the total of all name scores in the file.
    """
    try:
        with open('resources/documents/0022_names.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return "Error: names.txt not found. Please make sure the file is in the 'resources/documents/' directory."

    names = sorted([name.strip('"') for name in content.split(',')])
    
    total_score = 0
    for i, name in enumerate(names, 1):
        name_value = sum(ord(char) - ord('A') + 1 for char in name)
        name_score = name_value * i
        total_score += name_score
        
    return total_score

if __name__ == "__main__":
    print(solve())
