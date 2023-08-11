from random import randint


numbers = "1 99"
spliter = numbers.split(' ')
num_range = randint(int(spliter[0]), int(spliter[1]))
print(num_range)
num_test = input()


while num_test != 'd':

    if num_test == 'b':
        spliter[0] = num_range
        num_range = randint(int(spliter[0]), int(spliter[1]))
        print(num_range)
    elif num_test == 'k':
        spliter[1] = num_range
        num_range = randint(int(spliter[0]), int(spliter[1]))
        print(num_range)

    num_test = input()

