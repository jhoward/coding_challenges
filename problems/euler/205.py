import random

total = 0
wins = 0
draw = 0

while True:
    
    sFour = 0
    for i in range(9):
        sFour += int(random.random() * 4) + 1
        
    sSix = 0
    for i in range(6):
        sSix += int(random.random() * 6) + 1
        
    if sFour > sSix:
        wins += 1
    
    if sFour == sSix:
        draw += 1
        
    total += 1
    
    print str(total) + "   Win:" + str(wins/(total * 1.0)) + "     " + str(draw/(total * 1.0))
    
    