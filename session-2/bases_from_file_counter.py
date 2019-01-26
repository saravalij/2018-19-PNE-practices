
bases = ['A', 'C', 'T', 'G']
total_bases = 0


file = open('bases_file.txt', 'r')
content = file.read()
content = content.replace('\n', '')

for e in content:
    if e in bases:
        total_bases += 1
print('The total number of bases in the file is: ', total_bases)

for b in bases:
    print('{}: {}'.format(b, content.count(b)))