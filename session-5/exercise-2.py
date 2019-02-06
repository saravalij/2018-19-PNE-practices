def count_bases(seq):
    """Counting the number of each base in the sequence"""

    bases = ['A', 'C', 'G', 'T']
    times_b = []
    for b in bases:
        times_b.append(seq.count(b))

    # Return the result
    return dict(zip(bases, times_b))

# Main program
s1 = input('Please enter a sequence: ')
s2 = input('Please enter another sequence: ')
sequences = [s1, s2]

for sequence in sequences:
    print()
    # Print lengths identifying the number of each sequence
    print('Sequence {} is {} bases in length'.format(sequences.index(sequence)+1, len(sequence)))
    # Finding percentages
    for b in count_bases(sequence).keys():
        if len(sequence) > 0:
            perc = round(100.0 * count_bases(sequence)[b] / len(sequence), 1)
        else:
            perc = 0
# Printing results corresponding to one sequence at a time
        print("""Base {}
        Counter: {}
        Percentage: {}""".format(b, count_bases(sequence)[b], perc))
