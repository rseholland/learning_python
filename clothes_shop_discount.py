"Staff Discount for Clothes Shop Calculation 2"

"Step 1: Set Variables:"

staffDiscount = -40
calculatedDiscount = (1 + staffDiscount / 100)

"Set the prices of items"

coat1 = 400
coat2 = 250
coat3 = 175
top1 = 50
top2 = 75
top3 = 22.50
trousers1 = 75
trousers2 = 133
trousers3 = 99.99
jumper1 = 56
jumper2 = 97
jumper3 = 80
socks1 = 10
socks2 = 8
socks3 = 5
pants1 = 16
pants2 = 14.3
pants3 = 20
shoe1 = 80
shoe2 = 63.50
shoe3 = 56

"calculate the discount"

discountcoat1 = coat1 * calculatedDiscount
discountcoat2 = coat2 * calculatedDiscount
discountcoat3 = coat3 * calculatedDiscount
discounttop1 = top1 * calculatedDiscount
discounttop2 = top2 * calculatedDiscount
discounttop3 = top3 * calculatedDiscount
discounttrousers1 = trousers1 * calculatedDiscount
discounttrousers2 = trousers2 * calculatedDiscount
discounttrousers3 = trousers3 * calculatedDiscount
discountjumper1 = jumper1 * calculatedDiscount
discountjumper2 = jumper2 * calculatedDiscount
discountjumper3 = jumper3 * calculatedDiscount
discountsocks1 = socks1 * calculatedDiscount
discountsocks2 = socks2 * calculatedDiscount
discountsocks3 = socks3 * calculatedDiscount
discountpants1 = pants1 * calculatedDiscount
discountpants2 = pants2 * calculatedDiscount
discountpants3 = pants3 * calculatedDiscount
discountshoe1 = shoe1 * calculatedDiscount
discountshoe2 = shoe2 * calculatedDiscount
discountshoe3 = shoe3 * calculatedDiscount

"print outputs"

print("Retail price List: ")
print("Blue coat: £" + str(coat1)) 
print("Red coat: £" + str(coat2))
print("Green Rain Jacket: £" + str(coat3))
print("Stripy top: £" + str(top1))
print("Long sleeve: £" + str(top2))
print("Green t-shirt: £" + str(top3))
print("Navy cords: £" + str(trousers1))
print("Beige chinos: £" + str(trousers2))
print("Black jeans: £" + str(trousers3))
print("Woolly jumper: £" + str(jumper1))
print("Hooded jumper: £" + str(jumper2))
print("Green sweater: £" + str(jumper3))
print("White socks: £" + str(socks1))
print("Black socks: £" + str(socks2))
print("Grey socks: £" + str(socks3))
print("White pants: £" + str(pants1))
print("Black pants: £" + str(pants2))
print("Grey pants: £" + str(pants3))
print("Loafer: £" + str(shoe1))
print("Sneaker: £" + str(shoe2))
print("Brogues: £" + str(shoe3))

"print discounted prices"

print("")
print("Staff disocunt price list (40%): ")
print("Blue coat : £" + str(discountcoat1), "(savings = £" + str(coat1 - discountcoat1) + ")")
print("Red coat : £" + str(discountcoat2), "(savings = £" + str(coat2 - discountcoat2) + ")")
print("Green Rain Jacket: £" + str(discountcoat3), "(savings = £" + str(coat3 - discountcoat3) + ")")
print("Stripy top : £" + str(discounttop1), "(savings = £" + str(top1 - discounttop1) + ")")
print("Long sleeve : £" + str(discounttop2), "(savings = £" + str(top2 - discounttop2) + ")")
print("Green t-shirt : £" + str(discounttop3), "(savings = £" + str(top3 - discounttop3) + ")")
print("Navy cords : £" + str(discounttrousers1), "(savings = £" + str(trousers1- discounttrousers1) + ")")
print("Beige chinos : £" + str(discounttrousers2), "(savings = £" + str(trousers2 - discounttrousers2) + ")")
print("Black jeans : £" + str(discounttrousers3), "(savings = £" + str(trousers3 - discounttrousers3) + ")")
print("Woolly jumper : £" + str(discountjumper1), "(savings = £" + str(jumper1 - discountjumper1) + ")")
print("Hooded jumper : £" + str(discountjumper2), "(savings = £" + str(jumper2 - discountjumper2) + ")")
print("Green sweater : £" + str(discountjumper3), "(savings = £" + str(jumper3 - discountjumper3) + ")")
print("White socks : £" + str(discountsocks1), "(savings = £" + str(socks1 - discountsocks1) + ")")
print("Black socks : £" + str(discountsocks2), "(savings = £" + str(socks2 - discountsocks2) + ")")
print("Grey socks : £" + str(discountsocks3), "(savings = £" + str(socks3 - discountsocks3) + ")")
print("White pants : £" + str(discountpants1), "(savings = £" + str(pants1 - discountpants1) + ")")
print("Black pants : £" + str(discountpants2), "(savings = £" + str(pants2 - discountpants2) + ")")
print("Grey pants : £" + str(discountpants3), "(savings = £" + str(pants3 - discountpants3) + ")")
print("Loafer : £" + str(discountshoe1), "(savings = £" + str(shoe1 - discountshoe1) + ")")
print("Sneaker : £" + str(discountshoe2), "(savings = £" + str(shoe2 - discountshoe2) + ")")
print("Brogues : £" + str(discountshoe3), "(savings = £" + str(shoe3 - discountshoe3) + ")")
