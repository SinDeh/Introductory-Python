niter = int(input())   # Get the number of laptop entries
infos = []   # List to store laptop information

# Loop to collect laptop information
for _ in range(niter):
    laptop_info = input()   # Get input for laptop information
    integer = [int(i) for i in laptop_info.split()]   # Convert input to list of integers
    infos.append(integer)   # Append the laptop information to the list

x = 0   # Initialize a counter

# Nested loop to compare laptops
for n in range(niter):
    for m in range(niter):
        if (infos[n][0] < infos[m][0]) and (infos[n][1] > infos[m][1]):
            x += 1 

if x >= 1:
    print('happy irsa')
else:
    print('poor irsa')
