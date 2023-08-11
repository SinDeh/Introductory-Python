age1 = input()  # Get the first age input

list_age1 = ''  # Initialize an empty string to store ages as a list
maximum1 = ''   # Initialize the first maximum
maximum2 = ''   # Initialize the second maximum

while age1 != '-1':
    list_age1 += age1 + ' '  # Append the entered age to the list_age1
    spliter = list_age1.split(' ')  # Split the list_age1 into a list of ages
    maximum1 = int(max(spliter))   # Find the maximum among the current ages

    age1 = input()  # Get the next age input

maximum = max(spliter)  # Find the maximum age from the final list
spliter.remove(maximum)  # Remove the maximum age from the list
maximum2 = int(max(spliter))  # Find the second maximum age

# Print the two maximum ages
print(f'{maximum1} {maximum2}')
