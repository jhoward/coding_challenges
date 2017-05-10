import math

f = open('./files/base_exp.txt', "r")

values = []

for l in f.readlines():
    l = l.split(',')
    values.append(int(l[1]) * math.log10(int(l[0])))
    
    
tmpVal = sorted(values)
indexDict = dict([ (value, index) for index, value in enumerate(values)])

print [indexDict[entry] for entry in tmpVal]