from collections import OrderedDict

niter = int(input())   # Get the number of names to be entered

total_name = ''   # Initialize an empty string to store all the names

# Loop to collect names
for _ in range(niter):
    names = input()   # Get input name
    total_name += names + ' '   # Append the name to the total_name string

OrderedDict = {}   # Initialize an empty dictionary to store the name counts

# Loop to count the occurrences of each name and store them in the OrderedDict
for i in total_name.split():
    OrderedDict.setdefault(i, 0)   # Set the default value to 0 if the name is not already in the dictionary
    OrderedDict[i] += 1   # Increment the count of the name

# Loop to print the names and their respective counts, sorted alphabetically
for i, j in sorted(OrderedDict.items()):
    print(f'{i} {j}')
