x = int(input(""))   # Get input for the number to check
c = 0   # Initialize a counter

# Loop to check factors of x
for i in range(1, x):
    if (x % i == 0):   # If i is a factor of x
        c += 1   # Increment the counter

# Check if the counter is equal to 1
if (c == 1):
    print("prime")
else:
    print("not prime")
