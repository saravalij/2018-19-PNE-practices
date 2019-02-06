from Bases import count_bases

# Main program
s = input('Please enter the sequence: ')

# Print the total sequence length
print('This sequence is {} bases in length'.format(len(s)))

# Calculate the percentage of a base in the sequence and print results
for b in count_bases(s).keys():
    if len(s) > 0:
        perc = round(100.0 * count_bases(s)[b] / len(s), 1)
    else:
        perc = 0

    print("""Base {}
    Counter: {}
    Percentage: {}""".format(b, count_bases(s)[b], perc))