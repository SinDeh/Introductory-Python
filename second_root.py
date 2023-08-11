from math import sqrt   # Import the sqrt function from the math module

# Get the number of iterations
niter = int(input())

# Initialize an empty list to store the input numbers
list_number = []

# Loop to collect input numbers
for _ in range(niter):
    number = int(input())   # Get input number
    list_number.append(number)   # Append the number to the list

# Initialize an empty list to store the square roots of the numbers
num_root = []

# Loop to calculate the square roots of the numbers with 8 decimal places
for i in list_number:
    root = sqrt(i)   # Calculate the square root
    num_root.append(f'{root:.8f}')   # Append the formatted square root to the list

# Loop to print the square roots rounded to 4 decimal places
for j in num_root:
    print(j[:-4])
