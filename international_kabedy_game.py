player = input()   # Get input related to the player
play = input()     # Get input for the player's scores as a string
list_play = play.split()   # Split the scores into a list of strings
integer_play = list(map(int, list_play))   # Convert the strings to integers
range_play = 0   # Initialize a variable to count ranges

# Iterate through the player's scores
for i in integer_play:
    if i < 3:
        range_play += 1   # Increment the range count if the score is less than 3

# Calculate and print the number of ranges of 3 or more consecutive low scores
print(range_play // 3)
