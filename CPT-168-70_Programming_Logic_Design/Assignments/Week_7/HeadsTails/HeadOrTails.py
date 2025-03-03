from random import choice

# Declare the list of possible moves
moves = ["HEADS", "TAILS"]

# Loop 3 times
for _ in range(3):
    move_one = choice(moves)
    move_two = choice(moves)
    move_three = choice(moves)
    
    # Format the result
    result = f"{move_one} {move_two} {move_three}."
    
    # Print the result
    print(result)