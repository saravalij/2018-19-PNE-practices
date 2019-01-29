
bases = ['A', 'C', 'T', 'G']
total_bases = 0


file = open('CPLX2.txt', 'r')
content = file.read()
content = content.partition('\n')[2]
print(content)

for b in bases:
    print('{}: {}'.format(b, content.count(b)))