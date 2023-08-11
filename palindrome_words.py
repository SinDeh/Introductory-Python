word = input()   # Get input word
word = word.lower()   # Convert the word to lowercase
return_word = word[::-1]   # Reverse the word
return_word = return_word.lower()   # Convert the reversed word to lowercase

if word == return_word:
    print('palindrome')
else:
    print('not palindrome')
