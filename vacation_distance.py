numbers = input()   # Get input numbers as a string
list_number = numbers.split()   # Split the input string into a list of strings
list_number = list(map(int, list_number))   # Convert the list of strings to a list of integers

# Calculate the distance between the maximum and minimum values
distance = max(list_number) - min(list_number)

print(distance)   # Print the calculated distance
