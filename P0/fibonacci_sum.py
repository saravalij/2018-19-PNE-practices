
# from .fibonacci import fibonacci      why does it not work??

def fibonacci(n):
    if n == 0:
        print('Counting starts at term 1.')
        exit(1)
    elif n == 1:
        fibn = 0
    elif n == 2:
        fibn = 1
    else:
        fibn = [0, 1]
        for i in range(n-2):
            next = fibn[-2] + fibn[-1]
            fibn.append(next)
    return fibn

not_valid = True

while not_valid:
    try:
        nth_term = input('Type in the nth term you want to sum numbers up to: ')
        nth_term = int(nth_term)
        not_valid = False
    except:
        print('Oops. You must introduce a valid integer... Try again.')

numbers_to_n = fibonacci(nth_term)

total = 0

for i in numbers_to_n:
    total = total + i


print('The result of adding all fibonacci numbers up to term {} is {}.'.format(nth_term, total))