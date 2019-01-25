import math
import decimal

def compundInterestRateForDeposit(originalSum, annualInterestRate, frequency, timeLengthYears): 
  added = 1 + ( (annualInterestRate * 1.0) / frequency )
  totalPeriod = math.floor(frequency * (timeLengthYears / 12))
  accumulatedAdded = 1
  for i in range(1,totalPeriod + 1):
    accumulatedAdded = accumulatedAdded * added
  return math.ceil(originalSum * accumulatedAdded)

def printDifferentInterestRates(func):
  #interestRates = [1.5, 1.7, 2, 2.3, 2.7, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0, 9.0, 10.0]
  interestRates = [2.30]
  borrowedSums = [365000]
  numberOfYears = [28]
  for years in numberOfYears:
    for interestRate in interestRates:
      for borrowedSum in borrowedSums:
        func(borrowedSum, years, interestRate/100)

def loanWithInitialFixedRate(borrowedSum, totalYears, remaindingInterestRate, initialYears = 20, initialInterestRate = 0.0230):
  #calculate how much pay per month
  initialPayPerMonth = math.ceil(loanPaymentMonthly(borrowedSum, totalYears, initialInterestRate))
  #how much we have paid after initial period
  totalPayInitialPeriod = initialPayPerMonth * 12 * initialYears
  #calculate how much left to pay
  restToPay = round(principalAmountAfterNYears(borrowedSum, totalYears, initialYears, initialInterestRate),0)
  #calculate how much to pay per month for the next period 
  monthlyPayRemaindingPeriod = math.ceil(loanPaymentMonthly(restToPay, totalYears - initialYears, remaindingInterestRate))
  totalPayRemainingPeriod = monthlyPayRemaindingPeriod * 12 * (totalYears - initialYears)
  totalPay = totalPayInitialPeriod + totalPayRemainingPeriod
  print(f'sum: {borrowedSum} initialRate: {initialInterestRate}. Pay {initialYears} years = {initialPayPerMonth}, then {totalYears - initialYears} years = {monthlyPayRemaindingPeriod}. Remaining interest rate : {round(remaindingInterestRate,4)} To pay after {initialYears}: {restToPay} Total : {totalPay}')


def loanPaymentMonthly(borrowedSum, numberOfYears, interestRate):
  periodInterestRate = (1.0 * interestRate) / 12  
  numberPeriodicPayments = numberOfYears * 12
  cumulatedDiscount = 1
  for i in range(1,numberPeriodicPayments + 1):
    cumulatedDiscount = cumulatedDiscount * (1 + periodInterestRate)
  discount = (cumulatedDiscount - 1) / (periodInterestRate * cumulatedDiscount)
  monthlyPayment = math.ceil((1.0 * borrowedSum) / discount)
  return monthlyPayment

def loanPaymentMonthlyPrint(borrowedSum, numberOfYears, interestRate):
  monthlyPayment = loanPaymentMonthly(borrowedSum, numberOfYears, interestRate)
  print(f'{numberOfYears} years with interest rate: {interestRate} Monthly pay : {monthlyPayment} Total sum: {monthlyPayment * 12 * numberOfYears}')
  
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


print('#######################\n###Initial fixed rate###\n####################')
printDifferentInterestRates(loanWithInitialFixedRate)
print('###Clasic monthly payments###')
printDifferentInterestRates(loanPaymentMonthlyPrint)


def calculateMonthlyInterest(interestRate, loanPrincipal, years):
  monthlyInterestRate = interestRate * 1.0 / 12
  return (monthlyInterestRate ) * loanPrincipal

def calculateBalanceAfterOnePayment(loanPrincipal, monthlyRepayment, monthlyInterest):
  return loanPrincipal - (monthlyRepayment - monthlyInterest)

def calculateTilgung(loanPrincipal, maximumAmountPerMonthToPay, yearsWithFixedRate, yearlyInterestRate):
  monthlyInterest = calculateMonthlyInterest(yearlyInterestRate, loanPrincipal, yearsWithFixedRate)
  principal = loanPrincipal
  restToPay = 0
  for i in range(1, yearsWithFixedRate * 12 + 1):
    principal = calculateBalanceAfterOnePayment(principal, maximumAmountPerMonthToPay, monthlyInterest)
  restToPay = round(principal, 0)
  percentgePaid = ((loanPrincipal - restToPay) * 100.0) / loanPrincipal
  tilgung = round(percentgePaid / yearsWithFixedRate, 2) 
  return restToPay, tilgung
    
def showDifferentTilgungs():
  loanPrincipal = 365000
  maximumAmountPerMonth = 1672
  yearsWithFixedRate = 20
  yearlyInterestRate = 0.023
  restToPay, tilgung = calculateTilgung(loanPrincipal, maximumAmountPerMonth, yearsWithFixedRate, yearlyInterestRate)
  print(f'rest to pay: {restToPay} tilgung: {tilgung}') 

showDifferentTilgungs()