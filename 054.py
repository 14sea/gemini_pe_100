"""
Project Euler Problem 54: Poker hands

Problem:
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. How many hands does Player 1 win?

Solution Idea:
The core of the problem is to create a robust function that can evaluate a 5-card poker hand and assign it a rank that can be compared with another hand. The rank should account for both the hand type (e.g., Flush, Straight) and the values of the cards for tie-breaking.

1.  **Data Representation**:
    - A card (e.g., 'TH', 'AC') will be parsed into a numerical value and a suit.
    - Values are mapped: 2-9 -> 2-9, T -> 10, J -> 11, Q -> 12, K -> 13, A -> 14.
    - A hand is a list of 5 such parsed cards.

2.  **Ranking System**:
    - A hand's rank will be represented by a tuple. The first element is the primary rank of the hand (e.g., 9 for Royal Flush, 0 for High Card). Subsequent elements are for tie-breaking. Python's tuple comparison works element by element, which is perfect for this.
    - Ranks (from high to low):
        - 9: Royal Flush
        - 8: Straight Flush
        - 7: Four of a Kind
        - 6: Full House
        - 5: Flush
        - 4: Straight
        - 3: Three of a Kind
        - 2: Two Pairs
        - 1: One Pair
        - 0: High Card

3.  **Hand Evaluation Function (`get_hand_rank`)**:
    - This function will take a hand and return its rank tuple.
    - It first determines the hand's properties: are the cards a Straight? A Flush? How many cards of each value are there (e.g., one pair, two pairs)?
    - It then uses a series of `if/elif` statements, starting from the highest possible rank, to determine the hand's rank and construct the appropriate tuple with tie-breaker values.
    - For example, a Four of a Kind would return `(7, value_of_the_four, value_of_kicker)`. A Flush would return `(5, (sorted_card_values))`.

4.  **Main Loop**:
    - The main function reads the `poker.txt` file line by line.
    - For each line, it splits the cards into two hands for Player 1 and Player 2.
    - It calls the evaluation function for both hands.
    - It compares the resulting rank tuples. If Player 1's rank tuple is greater than Player 2's, a counter is incremented.
    - The final count is the answer.
"""

def get_hand_rank(hand):
    """
    Evaluates a 5-card poker hand and returns a comparable rank tuple.
    hand: A list of 5 (value, suit) tuples.
    """
    values = sorted([card[0] for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    
    is_flush = len(set(suits)) == 1
    
    # Straight check (handles Ace-low case)
    is_straight = False
    # A-low straight: A, 5, 4, 3, 2 -> values are [14, 5, 4, 3, 2]
    if values == [14, 5, 4, 3, 2]:
        is_straight = True
        # For ranking, treat Ace as low
        values = [5, 4, 3, 2, 1]
    # Normal straight
    elif len(set(values)) == 5 and values[0] - values[4] == 4:
        is_straight = True

    # Value counts for pairs, etc.
    value_counts = {v: values.count(v) for v in set(values)}
    counts = sorted(value_counts.values(), reverse=True)
    
    # Rank determination
    if is_straight and is_flush:
        # Royal flush is a straight flush with high card Ace (value 14)
        # The Ace-low straight case is handled by the re-assignment of `values`
        return (8, values[0]) # Rank 9 is implicitly handled by value
        
    if counts[0] == 4:
        four_val = [v for v, c in value_counts.items() if c == 4][0]
        kicker = [v for v, c in value_counts.items() if c == 1][0]
        return (7, four_val, kicker)
        
    if counts == [3, 2]:
        three_val = [v for v, c in value_counts.items() if c == 3][0]
        pair_val = [v for v, c in value_counts.items() if c == 2][0]
        return (6, three_val, pair_val)
        
    if is_flush:
        return (5, tuple(values))
        
    if is_straight:
        return (4, values[0])
        
    if counts[0] == 3:
        three_val = [v for v, c in value_counts.items() if c == 3][0]
        kickers = tuple(sorted([v for v, c in value_counts.items() if c == 1], reverse=True))
        return (3, three_val, kickers)
        
    if counts == [2, 2, 1]:
        pairs = sorted([v for v, c in value_counts.items() if c == 2], reverse=True)
        kicker = [v for v, c in value_counts.items() if c == 1][0]
        return (2, pairs[0], pairs[1], kicker)
        
    if counts[0] == 2:
        pair_val = [v for v, c in value_counts.items() if c == 2][0]
        kickers = tuple(sorted([v for v, c in value_counts.items() if c == 1], reverse=True))
        return (1, pair_val, kickers)
        
    return (0, tuple(values))

def solve():
    """
    Reads poker hands from a file, evaluates them, and counts Player 1's wins.
    """
    try:
        with open('resources/documents/0054_poker.txt', 'r') as f:
            hands_data = f.readlines()
    except FileNotFoundError:
        return "Error: poker.txt not found. Please make sure the file is in 'resources/documents/'."

    card_values = {r: i for i, r in enumerate('23456789TJQKA', 2)}
    p1_wins = 0

    for line in hands_data:
        cards = line.strip().split(' ')
        p1_hand_str = cards[:5]
        p2_hand_str = cards[5:]
        
        p1_hand = [(card_values[c[0]], c[1]) for c in p1_hand_str]
        p2_hand = [(card_values[c[0]], c[1]) for c in p2_hand_str]
        
        p1_rank = get_hand_rank(p1_hand)
        p2_rank = get_hand_rank(p2_hand)
        
        if p1_rank > p2_rank:
            p1_wins += 1
            
    return p1_wins

if __name__ == "__main__":
    print(solve())
