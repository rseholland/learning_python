"Tap BrothersLTD discount calculations"

"set variables"

firstDiscount = -25
firstCalculatedDiscount = (1 + firstDiscount / 100)
secondDiscount = -50
secondCalculatedDiscount = (1 + secondDiscount / 100)

"Beer prices (per can)"

boobieBeer = 3.5
forestFlavours = 4.25
sourMouth = 3.75
tenHundredYards = 3.0
trainToHell = 4.75
total = (boobieBeer + forestFlavours + sourMouth + tenHundredYards + trainToHell)

"Need to order 100 cans total to get discount - calculate price of 100 cans b4 discount"

hundredCansTotal = total * (100 / 5)
thousandCansTotal = total * (1000 / 5)


discountHundredCans = hundredCansTotal * firstCalculatedDiscount
discountThousandCans = thousandCansTotal * secondCalculatedDiscount

print("Total for 100 cans")
print(hundredCansTotal)
print("")
print("Total after discount (100 cans)")
print(discountHundredCans)
print("Total saved")
print(hundredCansTotal - discountHundredCans)
print("")
print("")
print("Total for 1000 cans")
print(thousandCansTotal)
print("")
print("Total after discount (1000 cans)")
print(discountThousandCans)
print("Total saved")
print(thousandCansTotal - discountThousandCans)



