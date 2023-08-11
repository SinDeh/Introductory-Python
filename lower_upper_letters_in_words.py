word = input()   # Get input word
upper = 0   # Initialize a counter for uppercase letters
lower = 0   # Initialize a counter for lowercase letters

# Loop to count uppercase and lowercase letters
for i in word:
    if i.islower():
        lower += 1
    else:
        upper += 1

# Check which case to convert the word
if upper > lower:
    print(word.upper())   # Convert to uppercase if there are more uppercase letters
elif lower > upper: 
    print(word.lower())   # Convert to lowercase if there are more lowercase letters
else:
    print(word.lower())   # Convert to lowercase if the counts are equal
