# Ask for input from the user
num = int(input())

# Convert the number to a string to extract the last digit
string_num = str(num)

# Get the last digit of the number
last = int(string_num[-1])

# Calculate the difference needed to reach the next multiple of 10
num_plus = 10 - last

# Add the difference to the input number
result = num + num_plus

# Display the result
print(result)
