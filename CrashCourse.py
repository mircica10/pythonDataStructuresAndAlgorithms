
import math

def repeat(s, numberOfTime = 3, exclamation=False):
  result = s
  for _ in range(1,numberOfTime):
    result = result + ' ' + s
  if exclamation:
    result = result + '!'
  return result

def testPrint(s):
  print(s + 'will be printed')

s = 'waka'
sRepeat = repeat(s)

assert 'waka waka waka' == sRepeat  

def printArray(max):
  arrayNumbers = ''
  for i in range(1, max):
    arrayNumbers = arrayNumbers + str(i)
  return arrayNumbers

assert printArray(4) == '123'

def playWithStrings():
  s = " hello,world "
  lengthS = len(s)
  print(lengthS)
  
  substring = s[3:7]
  print('substring from 3 to 7: ' + substring)

  print('substring stripped: '+ s.strip())

  print(f"string lower: {s.lower()}")
  print(f'string upper: {s.upper()}')
  print('string replate o with a: ' + s.replace('o', 'a'))
 
  arraySplitted = s.split(',')
  for sir in arraySplitted:
    print(sir)
#end play with strings

#play with lists
def playWithLists():
  myList = ['1', '2']
  print (myList)
  myList.append('3')
  print (myList)
  myList.append(['4', '5'])
  print (myList)
  myList.remove(['4','5'])
  print (myList)
  myList.extend(['4','5'])
  print(myList)
  print(f'index in a list: {myList.index("1")}')
  print(f'pop from the list: {myList.pop()}')
  myList.append('5')
  print(myList)
  myList += ['6', '7']
  print(myList)
  print(myList[2:])
  print(myList[:4])
  print(myList[::1])
  #loop in string
  for i in myList[::1]:
    print(i)

#playWithLists()

#Pnew = P(1 + r/n)power(n*t)
#P - original sum
#r - annualinterest rate
#n - frequncy - 12 for one year
#t - time legth years
def compundInterestRate(originalSum, annualInterestRate, frequency, timeLengthYears): 
  added = 1 + ( (annualInterestRate * 1.0) / frequency )
  totalPeriod = math.floor(frequency * (timeLengthYears / 12))
  accumulatedAdded = 1
  for i in range(1,totalPeriod + 1):
    accumulatedAdded = accumulatedAdded * added
  return math.ceil(originalSum * accumulatedAdded)



#testCompound = compundInterestRate(1500, 0.043, 4, 6)
#print(math.ceil(testCompound))


#testDifferentInterestRates()




#print(loanPaymentMonthly(100000, 30, 6))
#print(sumBack(100000, 30, 0.06))

#testDifferentInterestRates(loanPaymentMonthly)


#loanWithInitialFixedRate(100000, 25, 4.0, 5, 3.0)
#loanWithInitialFixedRate(450000, 25, 5.0)
