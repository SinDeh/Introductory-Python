letters = input()   # Get input string of letters
vowels = 'aeiou'   # Define a string containing the vowels
low_lettter = letters.lower()   # Convert the input letters to lowercase

# Remove vowels from the lowercase input letters
for i in vowels:
    low_lettter = low_lettter.replace(i, '')

# Print each remaining consonant with a period before it
for j in low_lettter:
    print('.' + j, end='')
