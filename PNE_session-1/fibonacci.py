
def fibonacci(n):
    n = int(n)
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

nth_term = input('Please, introduce the number of term to calculate: ')

print('\nTerm number {} of the fibonacci series is {}.'.format(nth_term, fibonacci(nth_term)[-1]))