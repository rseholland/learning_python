"set variables"

VAT = 25 ; calculatedVAT = (1 + VAT / 100)

"list prices"

netPriceOfMadoneSLR = 5600
netPriceOfDomaneSLR = 5000
netPriceOfEmondaSLR = 6000
netPriceOfMadoneSL = 3300
netPriceOfDomaneSL = 3000
netPriceOfEmondaSL = 3600

"calculate gross prices"

grossPriceOfMadoneSLR = netPriceOfMadoneSLR * calculatedVAT
grossPriceOfDomaneSLR = netPriceOfDomaneSLR * calculatedVAT
grossPriceOfEmondaSLR = netPriceOfEmondaSLR * calculatedVAT
grossPriceOfMadoneSL = netPriceOfEmondaSLR * calculatedVAT
grossPriceOfDomaneSL = netPriceOfMadoneSL * calculatedVAT
grossPriceOfEmondaSL = netPriceOfEmondaSL * calculatedVAT

"print outcome"

print(grossPriceOfMadoneSLR)
print(grossPriceOfDomaneSLR)
print(grossPriceOfEmondaSLR)
print(grossPriceOfMadoneSL)
print(grossPriceOfDomaneSL)
print(grossPriceOfEmondaSL)



