#Read data
data = []
with open('data.txt', 'r') as f:
    for rln in f:
        data.append([int(i) for i in rln.split(' ')])
        
