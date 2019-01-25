import sys
import math

def statements():
  a,b,c = "ABC"
  assert b == "B"
  t = [0,1]
  del t[0]
  assert len(t) == 1
  typeA = str(type(a))
  assert typeA == "<class 'str'>"

statements()

def numbersTest():
  imaginar = 4 + 2j
  assert imaginar.imag == 2
  assert 0xa == 10
  assert 5 / 2 == 2.5
  assert ~10 == -11
  assert 2<<2 == 8
  assert 2**3 == 8
  assert str(round(23.543, 1)) == "23.5"

numbersTest()

def dictionaryTest():
  dictionary = {'first':1, 'second':2}
  assert dictionary['first'] == 1
  assert len(dictionary) == 2
  assert ('first' in dictionary) == True
  assert dictionary.get('first') == 1

dictionaryTest()

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


evens = []
for i in range(1, 30):
  if i % 2 == 0:
    evens.append(i)

#list comprehension
evens2Digits = [i for i in evens if i > 10]

def listAsStack():
  myList = [1,2]
  myList.append(3)
  assert myList == [1,2,3]
  myList.pop()
  assert myList == [1,2]

listAsStack()

def listAsQueues():
  myList = [1,2]
  myList.append(3)
  assert myList == [1,2,3]
  myList.pop(0)
  assert myList == [2,3]

listAsQueues()  

import copy

def copyList():
  #shallow copy  -nested objects will not be copied
  myList = [1,2,[3,4]]
  newList = list(myList)
  newList[2][0] = 10
  assert myList == [1,2,[10,4]]
  #deep copy
  newList = copy.deepcopy(myList)
  newList[2][0] = 3
  assert myList == [1,2,[10,4]]
  assert newList == [1,2,[3,4]]

copyList()

