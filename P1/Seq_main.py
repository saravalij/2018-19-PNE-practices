from Seq import Seq

# Main program

s1 = Seq('AACTG')
s2 = Seq('GTCAATTCGCTGA')    # object from which we'll be getting the complementary and the reversed objects
s3 = s2.complement()
s4 = s2.reverse()

objs = [s1, s2, s3, s4]    # list containing all 4 objects

for o in objs:    # loop that will be printing all data that we are asked for, for each object
    print("""Sequence {}: {}
    Length: {}
    Bases count: A: {}, T: {}, C: {}, G: {} 
    Bases percentage: A: {}%, T: {}%, C: {}%, G: {}%
    """.format(objs.index(o)+1, o.strbase, o.len(), o.count('A'), o.count('T'), o.count('C'), o.count('G'),
               o.perc('A'), o.perc('T'), o.perc('C'), o.perc('G')))
