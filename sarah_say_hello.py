vorodi = input()   # Get input string
h1 = vorodi.find('h')   # Find the index of the first 'h'
h2 = vorodi.find('e', h1 + 1)   # Find the index of the first 'e' after 'h1'
h3 = vorodi.find('l', h2 + 1)   # Find the index of the first 'l' after 'h2'
h4 = vorodi.find('l', h3 + 1)   # Find the index of the second 'l' after 'h3'
h5 = vorodi.find('o', h4 + 1)   # Find the index of the first 'o' after 'h4'

# Check if the letters appear in the correct order and positions
TF = h1 >= 0 and h2 > h1 and h3 > h2 and h4 > h3 and h5 > h4

if TF:
    print('YES')
else:
    print('NO')
