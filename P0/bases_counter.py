
sequence = input('Introduce the sequence: ')
sequence = sequence.upper()

print('Total length: %s' % len(sequence))

bases = ['A', 'C', 'T', 'G']

for b in bases:
    print('{}: {}'.format(b, sequence.count(b)))
