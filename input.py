'''
"inputs as string"
a = input()
b = input()
c = input()

print(a + b + c)

"inputs as integers"

a = int(input())
b = int(input())
c = int(input())

'print(a + b + c) #casting allows you to change one type of variable to another'

'print("Sum of a and b is equal to:" + a + b + c) #won\'t work as there is string and integer'

print("Sum of a and b is equal to: " + str(a + b + c))
'''

print("Program that adds two numbers to each other")
a = int(input("first number: "))
b = int(input("second number: "))

print(a + b)
