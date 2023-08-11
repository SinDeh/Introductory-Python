def divisor(n):
    for i in range(n):
        x = len([i for i in range(1, n + 1) if not n % i])
    return x

nums = []   # List to store divisors
keys = {}   # Dictionary to store divisors as keys and corresponding numbers as values

for i in range(1, 21):   # Loop through 1 to 20
    preNum = int(input())   # Get user input for each number
    if preNum > 0:   # Check if the number is positive
        div = divisor(preNum)   # Calculate the number of divisors
        
    # If the div is not a key in keys or if it is and the current number is greater, update the keys
    if (div not in keys) or (div in keys and keys[div] < preNum):
        keys[div] = preNum
        nums.append(div)

nums.sort()   # Sort the list of divisors
max_div = nums[-1]   # Get the greatest divisor from the list
print(keys[max_div], max_div)   # Print the corresponding number and its greatest divisor
