import math

def testDifferentInterestRates(func):
  interestRates = [0.2, 0.5, 0.7, 1.0, 1.3, 1.5, 1.7, 2, 2.3, 2.7, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0, 9.0, 10.0]
  borrowedSums = [450000]
  numberOfYears = [15, 20, 25, 30]
  for years in numberOfYears:
    for interestRate in interestRates:
      for borrowedSum in borrowedSums:
        monthlyRate = math.ceil(func(borrowedSum, years, interestRate))
        totalSum = monthlyRate * 12 * years
        print(f'Sum:{borrowedSum} Years:{years} Rate:{interestRate} Total Sum:{totalSum} Monthly Rate:{monthlyRate}')


def printDifferentInterestRates(func):
  interestRates = [0.2, 0.5, 0.7, 1.0, 1.3, 1.5, 1.7, 2, 2.3, 2.7, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0, 9.0, 10.0]
  borrowedSums = [450000]
  numberOfYears = [20,25]
  for years in numberOfYears:
    for interestRate in interestRates:
      for borrowedSum in borrowedSums:
        func(borrowedSum, years, interestRate/100)

def loanWithInitialFixedRate(borrowedSum, totalYears, remaindingInterestRate, initialYears = 10, initialInterestRate = 0.002):
  #calculate how much pay per month
  initialPayPerMonth = math.ceil(loanPaymentMonthly(borrowedSum, totalYears, initialInterestRate))
  #how much we have paid after initial period
  totalPayInitialPeriod = initialPayPerMonth * 12 * initialYears
  #calculate how much left to pay
  restToPay = principalAmountAfterNYears(borrowedSum, totalYears, initialYears, initialInterestRate)
  #calculate how much to pay per month for the next period 
  monthlyPayRemaindingPeriod = math.ceil(loanPaymentMonthly(restToPay, totalYears - initialYears, remaindingInterestRate))
  totalPayRemainingPeriod = monthlyPayRemaindingPeriod * 12 * (totalYears - initialYears)
  totalPay = totalPayInitialPeriod + totalPayRemainingPeriod
  print(f'{initialYears} Y = {initialPayPerMonth}, then {totalYears - initialYears} Y = {monthlyPayRemaindingPeriod}. Remaining interest rate : {remaindingInterestRate} Total : {totalPay}')


def loanPaymentMonthly(borrowedSum, numberOfYears, interestRate):
  periodInterestRate = (1.0 * interestRate) / 12  
  numberPeriodicPayments = numberOfYears * 12
  cumulatedDiscount = 1
  for i in range(1,numberPeriodicPayments + 1):
    cumulatedDiscount = cumulatedDiscount * (1 + periodInterestRate)
  discount = (cumulatedDiscount - 1) / (periodInterestRate * cumulatedDiscount)
  monthlyPayment = math.ceil((1.0 * borrowedSum) / discount)
  print(f'{numberOfYears} years with interest rate: {interestRate} Monthly pay : {monthlyPayment} Total sum: {monthlyPayment * 12 * numberOfYears}')
  return monthlyPayment


#https://en.wikipedia.org/wiki/Amortization_calculator
def principalAmountAfterNYears(totalSum, totalPeriodYears, partialPeriodYears, interestRate):
  totalPeriodMonths = totalPeriodYears * 12
  partialPeriodMonths = partialPeriodYears * 12
  interestRatePerPeriod = interestRate / 12
  #(1+i)pow(t)
  nominator = 1
  for i in range(1, partialPeriodMonths + 1):
    nominator *= (interestRatePerPeriod + 1 )
  #(1+i)pow(n)
  denominator = 1
  for i in range(1, totalPeriodMonths + 1):
    denominator *= (interestRatePerPeriod + 1)
  principalAmount = totalSum * ( 1 - (nominator - 1) / (denominator - 1) )
  return principalAmount

print('###Initial fixed rate###')
printDifferentInterestRates(loanWithInitialFixedRate)
print('###Clasic monthly payments###')
printDifferentInterestRates(loanPaymentMonthly)


#print(principalAmountAfterNYears(100000, 300, 60, 0.03))
#print(loanWithInitialFixedRate(100000, 25, 0.04, 5, 0.03))

