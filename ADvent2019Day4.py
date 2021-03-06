MAX_LEN = 6
MAX_VALUE = 9
solCount = 0
INPUT_LOW = 136760
INPUT_HIGH = 595730

def lastElem(lst):
    length = len(lst)
    return 1 if length == 0 else lst[length - 1]

def hasConsecutiveDoubles(lst):
    for i in range(len(lst) - 1):
        if (lst[i] == lst[i + 1]):
            return True
    return False   


def hasConsecutiveDoublesEven2(lst):
    hasDouble = False
    last = 0
    nrOccurences = 1
    for i in lst:
        if ( i == last):
            nrOccurences += 1
        else:
            if(nrOccurences == 2):
            	hasDouble = True
            nrOccurences = 1
        last = i
    if (nrOccurences == 2):
    	hasDouble = True
    return hasDouble    

#must be at least one with 2 only
def hasConsecutiveDoublesEven(lst):
    isDoublePresent = False
    countSame = 0
    i = 1
    while (i < len(lst)):
        while ( i < len(lst) and lst[i] == lst[i - 1] ):
            countSame += 1
            i += 1
        if (countSame == 1):
            isDoublePresent = True
        countSame = 0    
        i += 1
    return isDoublePresent
    
def convertArrayToInt(array):
    number = 0
    power = 1
    array = reversed(array)
    for i in array:
        number = number + i * power
        power = power * 10
    return number    

def calculateAdventDay4(step, tempSol):
    global solCount
    if(step == MAX_LEN):
        hasDoubles = hasConsecutiveDoublesEven(tempSol)
        number = convertArrayToInt(tempSol)
        if(number >= INPUT_LOW and number <= INPUT_HIGH and hasDoubles):            
            solCount = solCount + 1
            #print(number)
            return            
        return          
    for i in range(lastElem(tempSol), MAX_VALUE + 1):
            tempSol.append(i)
            calculateAdventDay4(step + 1, tempSol)
            tempSol.pop()
    

def calculateAdventDay4Help(): 
    step = 0
    tempSol = []
    calculateAdventDay4(step, tempSol)
    print(solCount)
  

calculateAdventDay4Help() 
