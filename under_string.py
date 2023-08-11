word = input()   # Get input string

# Check if both 'AB' and 'BA' are present in the input string
if word.find('AB') != -1 and word.find('BA') != -1:
    # Check if 'AB' appears before 'BA'
    if word.find('AB') < word.find('BA'):
        word = word.replace('AB', '', 1)   # Remove one occurrence of 'AB'
        # Check if 'BA' still appears in the remaining string
        if 'BA' in word:
            print('YES')
        else:
            print('NO')

    # Check if 'BA' appears before 'AB'
    elif word.find('AB') > word.find('BA'):
        word = word.replace('BA', '', 1)   # Remove one occurrence of 'BA'
        # Check if 'AB' still appears in the remaining string
        if 'AB' in word:
            print('YES')
        else:
            print('NO')

# Check if only 'BA' is present in the input string
elif word.find('AB') == -1 and word.find('BA') != -1:
    print('NO')

# Check if only 'AB' is present in the input string
elif word.find('AB') != -1 and word.find('BA') == -1:
    print('NO')

# If neither 'AB' nor 'BA' is present in the input string
else:
    print('NO')
