"Staff Discount calculation"

"set variables"

staffDiscount = -35
calculatedDiscount = (1 + staffDiscount / 100)

"set prices"

shoes = 106
top = 125
helmet = 200
gloves = 25
shorts = 225
socks = 10
total = (shoes + top + helmet + gloves + shorts + socks)

"calulate discount"

discountShoes = shoes * calculatedDiscount
discountTop = top * calculatedDiscount
discountHelmet = helmet * calculatedDiscount
discountGloves = gloves * calculatedDiscount
discountShorts = shorts * calculatedDiscount
discountSocks = socks * calculatedDiscount

"print outputs"

print("Shoes = 106")
print("Top = 125")
print("Helmet = 200")
print("Gloves = 25")
print("Shorts = 225")
print("Socks = 10")

print("Total before discount")
print(total)

print("Staff discount = 35%")
print("Total after discount")
discountedTotal = discountShoes + discountTop + discountHelmet + discountGloves + discountShorts + discountSocks
print(discountedTotal)
print("Money saved =");print(total - discountedTotal)




