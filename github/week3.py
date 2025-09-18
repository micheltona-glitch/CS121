
'''number = 5
max_number = int(input("ENter a number: "))
while number <= max_number:
    if number % 2 == 1:
        print(number)
    number += 1
'''

'''a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

# Compare and swap manually
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print("Increasing order:", a, b, c)
'''
#shit i gotta remember 

knuts = int(input("Enter amount of knuts: "))

galleons = knuts // 493
remaining = knuts % 493

sickles = remaining // 29
knuts_left = remaining % 29
if galleons > 0:
    print(galleons, "galleon" if galleons == 1 else "galleons", end=" ")
if sickles > 0:
    print(sickles, "sickle" if sickles == 1 else "sickles", end=" ")
if knuts_left > 0:
    print(knuts_left, "knut" if knuts_left == 1 else "knuts", end=" ")
  