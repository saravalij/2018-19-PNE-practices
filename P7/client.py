import http.client
import termcolor
import json
from P1.Seq import Seq


conn = http.client.HTTPConnection('rest.ensembl.org')

conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

r1 = conn.getresponse()

print("Response received!: {} {}\n".format(r1.status, r1.reason))

data1 = r1.read().decode("utf-8")

r1.close()

gen_data = json.loads(data1)

seq = gen_data['seq']

seq = Seq(seq)

print('There are {} bases in the FRAT1 gene.'.format(seq.len()))

print('Number of T bases: {}.'.format(seq.count('T')))

bases = ['A','C','G','T']
great = 0

for b in bases:
    if seq.count(b) > great:
        great = seq.count(b)
        popular = b

print('The most popular base in the sequence is {}, being its percentage {}%.'.format(popular, seq.perc(popular)))

for b in bases:
    print('Percentage of {} is: {}.'.format(b, seq.perc(b)))
