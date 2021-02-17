"""
Arithmetic operators

+ = add
- = subtraxt
* = multiply
/ = divide

() - parenthesis - for changing order of maths operation (BIDMAS)
"""
VAT = 25

netPriceOfShoes = 100
netPriceOfTV = 2000

grossPriceOfShoes = netPriceOfShoes * (1 + VAT/100)
grossPriceOfTV = netPriceOfTV * (1 + VAT/100)

"By stating VAT, If VAT was to then change, we can make sure code written reflects this"

VAT = 20

netPriceOfShoes = 100
netPriceOfTV = 2000

grossPriceOfShoes = netPriceOfShoes * (1 + VAT/100)
grossPriceOfTV = netPriceOfTV * (1 + VAT/100)

"The expression (1 + VAT/100) will not change so we create another variable called calculatedVAT"

VAT = 20
calculatedVAT = (1 + VAT / 100)

netPriceOfShoes = 100
netPriceOfTV = 2000

grossPriceOfShoes = netPriceOfShoes * calculatedVAT
grossPriceOfTV = netPriceOfTV * calculatedVAT

