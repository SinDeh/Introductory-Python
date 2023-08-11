numbers = input()   # Get input string of numbers separated by '+'
spliter = numbers.split('+')   # Split the input string into a list of numbers
spliter.sort()   # Sort the list of numbers

string_spliter = ''.join(spliter)   # Join the sorted list without separators
string_spliter = '+'.join(string_spliter)   # Join the sorted list with '+' signs as separators
print(string_spliter)   # Print the final reassembled string
