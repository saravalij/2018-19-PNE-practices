
def fibonacci(n):
    n = int(n)
    if n == 0:
        fibn = 0
    elif n == 1:
        fibn = 1
    else:
        fibn = 0
        prev = 0
        for i in range(n):
            prev = i + prev
            print(prev)
        fibn = prev
    return fibn

nth_term = input('Please, introduce the number of term to calculate: ')

print('The {}th fibonacci number is {}.'.format(nth_term, fibonacci(nth_term)))