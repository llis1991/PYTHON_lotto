
import random
'''
def losowanieLotto(numbersOfBalls, BallsToDraw):
    lottoList = []
    for i in range(0, BallsToDraw):
        drawNumber = random.randint(1, numbersOfBalls)
        if drawNumber not in lottoList:
            lottoList.append(drawNumber)
        elif drawNumber in lottoList:
            
    return lottoList

print(losowanieLotto(49, 6))


for i in range(0, a==5):
        drawNumber = random.randint(1, 10)
        if drawNumber < 5:
            print(drawNumber)
        elif drawNumber > 5:


liczba = 0
while liczba < 5:
    drawNumber = random.randint(0, 10)
    if drawNumber < 5:
        print(drawNumber)
        liczba += 1
    elif drawNumber > 5:
        liczba -= 1
'''

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

    
