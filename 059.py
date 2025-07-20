"""
Project Euler Problem 59: XOR decryption

Problem:
The file 0059_cipher.txt contains a message encrypted with a repeating three-letter lowercase key. Decrypt the message and find the sum of the ASCII values of the original text. The original text is known to contain common English words.

Solution Idea:
The key is a repeating sequence of three lowercase letters. This means the first character of the key encrypts the 1st, 4th, 7th, ... characters of the message. The second character of the key encrypts the 2nd, 5th, 8th, ... characters, and so on. This structure allows us to break the problem down into three independent sub-problems.

1.  **Read the Ciphertext**: Read the comma-separated ASCII values from the file into a list of integers.

2.  **Brute-Force the Key**: Since the key consists of three lowercase English letters, there are only `26 * 26 * 26 = 17,576` possible keys. This is a small enough number to brute-force.

3.  **Frequency Analysis (The "English Words" Clue)**: The most crucial clue is that the decrypted text contains common English words. This implies that the decrypted text will have a character frequency distribution similar to that of standard English text. The most common character in English is the space character (' ').
    - We can try every possible key. For each key, we decrypt the message.
    - We then analyze the decrypted text. A good heuristic is that the correct key will produce a decrypted text with a very high frequency of spaces, or other common letters like 'e', 't', 'a'.
    - We can iterate through all possible keys, decrypt the text, and score the result based on how "English-like" it is. The key that produces the highest score is very likely the correct one.

4.  **Algorithm**:
    a.  Parse the cipher file into a list of integers.
    b.  Generate all possible three-letter lowercase keys (from 'aaa' to 'zzz').
    c.  For each potential `key`:
        i.   Create the full, repeating key stream that is the same length as the ciphertext.
        ii.  XOR the ciphertext with the key stream to produce a potential plaintext.
        iii. Count the occurrences of common English characters (especially space) in the plaintext.
    d.  The key that produces the plaintext with the highest count of spaces is almost certainly the correct key.
    e.  Once the correct key is found, decrypt the entire message with it.
    f.  Calculate the sum of the ASCII values of the characters in the decrypted message.
"""
import itertools

def solve():
    """
    Decrypts the message in 0059_cipher.txt and finds the sum of the ASCII values.
    """
    try:
        with open('resources/documents/0059_cipher.txt', 'r') as f:
            cipher_text = [int(c) for c in f.read().strip().split(',')]
    except FileNotFoundError:
        return "Error: 0059_cipher.txt not found. Please ensure it's in the 'resources/documents/' directory."

    best_key = ''
    max_spaces = 0
    
    # Generate all possible 3-letter lowercase keys
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    for key_tuple in itertools.product(lowercase_chars, repeat=3):
        key = "".join(key_tuple)
        key_ascii = [ord(c) for c in key]
        
        decrypted_text = []
        space_count = 0
        
        for i in range(len(cipher_text)):
            decrypted_char_code = cipher_text[i] ^ key_ascii[i % 3]
            decrypted_text.append(decrypted_char_code)
            if decrypted_char_code == ord(' '):
                space_count += 1
        
        if space_count > max_spaces:
            max_spaces = space_count
            best_key = key

    # Now decrypt with the best key and sum the ASCII values
    best_key_ascii = [ord(c) for c in best_key]
    total_ascii_sum = 0
    for i in range(len(cipher_text)):
        decrypted_char_code = cipher_text[i] ^ best_key_ascii[i % 3]
        total_ascii_sum += decrypted_char_code
        
    return total_ascii_sum

if __name__ == "__main__":
    print(solve())
