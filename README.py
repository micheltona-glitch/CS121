printimport math 
''''
human_year = input("Enter your age: ")
dog_year = float(human_year) * 7
dog_year2 = dog_year - int(dog_year)
dog_month = dog_year2 * 12
dog_month2 = dog_month - int(dog_month)
dog_days = dog_month2 * 30



dog_year_ = int(dog_year)
dog_month_ = int(dog_month)
dog_days_ = int(dog_days)

print(f"Your age {human_year} in dogs years is {dog_year_} years, {dog_month_} months, {dog_days_} days")


 
a= 10
b = 15
h = 5
area = ((a + b)/2) * h

print(f"area is {area}")

r = 10

volume = (4/3)*math.pi* (r**3)
print(f"volume is {volume}") '''

MS = int(input("enter the standards: "))
if MS >= 57:
    print("A+")    
elif MS <= 53:
    if MS >= 51:
        print("A-")
    elif MS >= 49:
        print("B+") 
    elif MS>= 47:
        print("B")
    elif MS>= 45:
        print("B-")
    elif MS>= 43:
        print("C+")
    elif MS>= 40:
        print("C")
    elif MS>= 35:
        print('D')
    elif MS < 35:
        print("F")
    else:
        print("nothing")
else:
    print("")                

