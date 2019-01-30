
bases = ['A', 'C', 'T', 'G']
content = []

for line in open('CPLX2.txt', 'r'):
    if line.startswith('>'):
        continue
    else:
        content.append(line)

content = ''.join(content)

for b in bases:
    print('{}: {}'.format(b, content.count(b)))