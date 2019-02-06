def count_bases(seq):
    """Counting the number of each base in the sequence"""

    bases = ['A', 'C', 'G', 'T']
    times_b = []
    for b in bases:
        times_b.append(seq.count(b))

    # Return the result
    return dict(zip(bases, times_b))