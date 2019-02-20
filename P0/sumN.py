

def sumn(n):
    total = 0
    try:
        n = int(n)
    except:
        print('Error.')
    else:
        for element in range(n):
            total = total + (element+1)
        return total


n_integers = input('Type in the integer to which you want to sum: ')

print('The result of summing the first', n_integers, 'integers is: ', sumn(n_integers))