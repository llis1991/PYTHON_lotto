
import random

def losowanieLotto(numbersOfBalls, ballsToDraw):
    lottoList = []
    i = 0
    while i < ballsToDraw:
        drawNumber = random.randint(1, numbersOfBalls)
        if lottoList.count(drawNumber)==0:
            lottoList.append(drawNumber)
            i+=1
            
    return lottoList

print(losowanieLotto(49, 6))

    
