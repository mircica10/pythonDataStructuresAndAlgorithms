
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
testPrint(s)
sRepeat = repeat(s)

assert 'waka waka waka' == sRepeat  

def printArray(max):
  arrayNumbers = ''
  for i in range(1, max):
    arrayNumbers = arrayNumbers + str(i)
  return arrayNumbers

assert printArray(4) == '123'
