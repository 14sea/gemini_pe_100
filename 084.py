"""
Project Euler Problem 84: Monopoly odds

Problem:
Simulate a game of Monopoly using two 4-sided dice. Find the three most frequently visited squares and form a six-digit modal string from their square numbers (e.g., 102400).

The rules are:
- Start at GO (00).
- Roll two 4-sided dice to move.
- Landing on G2J (30) sends you to JAIL (10).
- Rolling three consecutive doubles sends you to JAIL.
- Community Chest (CC) squares (2, 17, 33) have 2/16 cards that move you.
- Chance (CH) squares (7, 22, 36) have 10/16 cards that move you.

Solution Idea:
We can simulate the game for a large number of turns to find the steady-state probabilities of landing on each square. This is a Monte Carlo simulation of a Markov chain.

1.  **Board Representation**:
    - The 40 squares can be represented by an array or list, indexed 0 to 39.
    - We'll need to map square names (like 'G2J', 'CC1', 'CH1') to their indices.

2.  **Simulation Loop**:
    - We'll simulate a large number of dice rolls (e.g., 1,000,000) to get a good statistical sample.
    - We need to keep track of the player's `current_position`, the number of `consecutive_doubles`, and the visit counts for each square.

3.  **Handling Game Logic**:
    a.  **Dice Roll**: In each turn, roll two 4-sided dice. Check if it's a double.
    b.  **Three Doubles Rule**: If it's the third consecutive double, send the player to JAIL and reset the doubles counter. Otherwise, advance the player.
    c.  **G2J**: If the player lands on G2J, move them to JAIL.
    d.  **Community Chest (CC)**:
        - If the player lands on a CC square, we simulate drawing a card. There's a 2/16 chance of a move.
        - We can use a random number generator. If `rand(1, 16) <= 2`, a move occurs.
        - If `rand(1, 16) == 1`, go to GO. If `== 2`, go to JAIL. Otherwise, stay put.
    e.  **Chance (CH)**:
        - If the player lands on a CH square, there's a 10/16 chance of a move.
        - We handle each of the 10 movement cards: Go to GO, JAIL, C1, E3, H2, R1, next R, next U, back 3.
        - "Next R" and "Next U" require finding the index of the next railway or utility square from the current position.

4.  **Final Analysis**:
    - After the simulation, we will have an array of visit counts for each square.
    - We find the indices of the three squares with the highest counts.
    - We sort these three squares in descending order of their visit counts.
    - We format their indices as two-digit strings and concatenate them to form the final six-digit modal string.
"""
import random

def solve():
    """
    Simulates Monopoly with two 4-sided dice to find the three most popular squares.
    """
    # Board layout and special squares
    squares = list(range(40))
    GO, JAIL, G2J = 0, 10, 30
    C1, E3, H2, R1 = 11, 24, 39, 5
    CC = {2, 17, 33}
    CH = {7, 22, 36}
    R = {5, 15, 25, 35}
    U = {12, 28}

    # Simulation parameters
    num_turns = 1_000_000
    visit_counts = [0] * 40
    current_pos = 0
    consecutive_doubles = 0

    for _ in range(num_turns):
        # Roll two 4-sided dice
        d1 = random.randint(1, 4)
        d2 = random.randint(1, 4)
        
        if d1 == d2:
            consecutive_doubles += 1
        else:
            consecutive_doubles = 0
            
        if consecutive_doubles == 3:
            current_pos = JAIL
            consecutive_doubles = 0
        else:
            current_pos = (current_pos + d1 + d2) % 40
            
            # Handle special landings
            if current_pos in CC:
                card = random.randint(1, 16)
                if card == 1: current_pos = GO
                elif card == 2: current_pos = JAIL
            
            elif current_pos in CH:
                card = random.randint(1, 16)
                if card == 1: current_pos = GO
                elif card == 2: current_pos = JAIL
                elif card == 3: current_pos = C1
                elif card == 4: current_pos = E3
                elif card == 5: current_pos = H2
                elif card == 6: current_pos = R1
                elif card in [7, 8]: # Next R
                    if current_pos == 7: current_pos = 15
                    elif current_pos == 22: current_pos = 25
                    else: current_pos = 5 # from 36
                elif card == 9: # Next U
                    if current_pos == 7 or current_pos == 36: current_pos = 12
                    else: current_pos = 28 # from 22
                elif card == 10: # Back 3
                    current_pos = (current_pos - 3 + 40) % 40

            elif current_pos == G2J:
                current_pos = JAIL

        visit_counts[current_pos] += 1

    # Find the top three squares
    indexed_counts = sorted([(count, i) for i, count in enumerate(visit_counts)], reverse=True)
    
    modal_string = ""
    for i in range(3):
        modal_string += f"{indexed_counts[i][1]:02d}"
        
    return modal_string

if __name__ == "__main__":
    print(solve())
