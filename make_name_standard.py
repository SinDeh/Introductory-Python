on_title = ''   # Initialize an empty string to store names with title casing

# Loop to collect names
for _ in range(10):
    name = input()   # Get input for each name
    on_title += name + ' '   # Append the name to the on_title string, separated by a space

list_name = on_title.split()   # Split the on_title string into a list of names

# Loop to capitalize the first letter of each name
for i in list_name:
    print(i.title())   # Print the name with title casing
