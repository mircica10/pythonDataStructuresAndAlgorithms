def calculateAveragePriceHelper():
  priceAndArea = [(31000, 36),(40000, 54),(47000, 54),(49500,50),
  (36000,38),(52000,54),(42000,40),(33000,37),(37000,37),(39000,50),(54500, 48)]
  average = calculateAveragePrice(priceAndArea)
  pretMediu = average * 47.23
  print(f'media:{average} pret mediu:{pretMediu}')

def calculateAveragePrice(apartments):
  averageList = []
  for apartment in apartments:
    area = apartment[1]
    price = apartment[0]
    average = price * 1.0 / area
    averageList.append(average)
  priceSum = sum(averageList)
  priceCount = len(averageList)  
  return priceSum / priceCount

calculateAveragePriceHelper()
