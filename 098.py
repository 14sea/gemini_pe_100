
from collections import defaultdict

def get_words(path):
    with open(path, 'r') as f:
        content = f.read()
        words = [word.strip('"') for word in content.split(',')]
    return words

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        anagrams[key].append(word)
    return {k: v for k, v in anagrams.items() if len(v) > 1}

def get_squares(max_len):
    squares = defaultdict(list)
    i = 1
    while len(str(i*i)) <= max_len:
        s = i*i
        squares[len(str(s))].append(s)
        i += 1
    return squares

def find_largest_square_anagram(words_path):
    words = get_words(words_path)
    anagram_groups = group_anagrams(words)
    if not anagram_groups:
        return 0
    max_len = max(len(k) for k in anagram_groups.keys())
    squares_by_len = get_squares(max_len)
    
    max_square = 0

    for key, anagrams in anagram_groups.items():
        word_len = len(key)
        for square in squares_by_len[word_len]:
            s_square = str(square)
            if len(set(key)) != len(set(s_square)):
                continue

            for w1_idx, w1 in enumerate(anagrams):
                mapping = {}
                valid_map = True
                temp_s_square = s_square
                
                # Try to map w1 to s_square
                for i in range(word_len):
                    char = w1[i]
                    digit = temp_s_square[i]
                    if char in mapping and mapping[char] != digit:
                        valid_map = False
                        break
                    if char not in mapping and digit in mapping.values():
                        valid_map = False
                        break
                    mapping[char] = digit
                
                if not valid_map:
                    continue

                for w2_idx, w2 in enumerate(anagrams):
                    if w1_idx == w2_idx:
                        continue

                    num_str = ""
                    for char in w2:
                        num_str += mapping[char]
                    
                    if num_str.startswith('0'):
                        continue

                    num = int(num_str)
                    if num in squares_by_len[word_len]:
                        max_square = max(max_square, square, num)
    
    return max_square

def main():
    words_path = 'resources/documents/0098_words.txt'
    try:
        result = find_largest_square_anagram(words_path)
        print(result)
    except FileNotFoundError:
        print(f"Error: The file '{words_path}' was not found.")

if __name__ == "__main__":
    main()
