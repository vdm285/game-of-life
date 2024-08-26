import time
import os
import random

# Create a translation table for all possible combinations of current state and live neighbors
def make_translation_table():
    translation_table = {}
    for state in ['0', '1']:
        for neighbors in range(9):  # There can be 0 to 8 neighbors
            key = f"{state}{neighbors}"
            if state == '1':  # Live cell
                translation_table[key] = '1' if 2 <= neighbors <= 3 else '0'
            else:  # Dead cell
                translation_table[key] = '1' if neighbors == 3 else '0'
    return translation_table

# Function to count live neighbors in a 1D string
def count_live_neighbors(state, index):
    neighbors = [
        -9, -8, -7, # Above row neighbors
        -1,     1,  # Side neighbors
        7,  8,  9   # Below row neighbors
    ]
    live_count = 0
    row = index // 8
    
    for n in neighbors:
        neighbor_index = index + n
        
        # Handle wrapping at the edges of the grid
        if neighbor_index < 0 or neighbor_index >= 64:
            continue
        
        # Ensure the neighbor isn't from a different row
        neighbor_row = neighbor_index // 8
        if abs(neighbor_row - row) > 1:
            continue
        
        # Check if the neighbor is alive
        if state[neighbor_index] == '1':
            live_count += 1
            
    return live_count

# Function to update the game state using str.translate
def update_state(state, translation_table):
    new_state = []
    for i in range(64):
        live_neighbors = count_live_neighbors(state, i)
        new_state.append(translation_table[f"{state[i]}{live_neighbors}"])
    return ''.join(new_state)

# Function to print the current game state with ASCII squares
def print_state(state):
    for i in range(0, 64, 8):
        row = state[i:i+8]
        print("  ".join('■' if cell == '1' else '□' for cell in row))

# Generate a random 64-character binary string
state = ''.join(random.choice('01') for _ in range(64))

# Create the translation table
translation_table = make_translation_table()

# Main loop to run the game
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    print_state(state)
    state = update_state(state, translation_table)
    time.sleep(1)
