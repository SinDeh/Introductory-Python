import numpy as np

# Initialize NumPy arrays to store total score and total wins
total_score = np.zeros((1, 1))
total_win = np.zeros((1, 1))

# Iterate through 30 games
for _ in range(30):
    score = input()  # Get the user input for the score of each game
    
    if (score == '1') or (score == '3'):
        total_score += int(score)  # Increment total score for wins and ties
    
    if (score == '3'):
        total_win += int(score)  # Increment total wins for only wins

# Print the calculated total score and number of wins
print(f'{int(total_score)} {int(total_win/3)}')
