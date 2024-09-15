import random

# Sap Sidi ka Board
board = {3: 22, 5: 8, 11: 26, 20: 29, 17: 4, 19: 7, 27: 1, 21: 9, 34: 6, 51: 67, 71: 91, 78: 100, 92: 76, 95: 24}

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player_position = 0
    while player_position < 100:
        input("Press enter to roll the dice: ")
        dice_value = roll_dice()
        print(f"Dice rolled: {dice_value}")
        player_position += dice_value
        
        if player_position > 100:
            player_position -= dice_value  # If exceeding 100, stay at current position
        
        if player_position in board:
            if player_position < board[player_position]:
                print(f"Yay! Ladder at {player_position}, climbing to {board[player_position]}")
            else:
                print(f"Oh no! Snake at {player_position}, sliding to {board[player_position]}")
            player_position = board[player_position]
        
        print(f"You're now at position {player_position}")
    
    print("Congratulations! You've reached 100!")

play_game()