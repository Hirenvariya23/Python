print("Hello"[3])       # starts with 0
print(1_00_00_000 + 456)       # underscore is just to make code readable
print("Type of len = " + str(type(input("What is your name?"))))  # <class 'int'>
print("Type of len = " + str(type(len(input("What is your name?")))))  # <class 'int'>
print(70 + float("100.25"))  # 170.25
print(6 / 3)            # 2.0 always float with division
print(2 ** 3)           # exponent o/p 8
print(88 ** 4)           # exponent o/p 8
print(round(2.6666, 2)) # 2.67
print(round(2.6789, 3)) # 2.67
 # //: divide with integral result (discard remainder)
print(8 // 3)           # 2 int instead of float
print(12 // 3)           # 2 int instead of float 
print(19 // 3)           # 2 int instead of float

age = int(input("Enter your age: "))
lifeLeft = (90 - age) * 52 
print(f"You have {lifeLeft} weeks left.")
print("You have " + str(lifeLeft) + " weeks left.")    #str is used to covert to string

fTotalBill = float(input("How much is the total bill? $"))
iNoOfPeople = int(input("How many no of people? "))
iTipPercentage = int(input("How much is the tip percentage? "))
fPerPersonBill = (fTotalBill + (fTotalBill * (iTipPercentage / 100))) / iNoOfPeople
fPerPersonBill = "{:.2f}".format(fPerPersonBill)    # round(fPerPersonBill, 2)
print(f"Per person bill = ${fPerPersonBill}")
hotel = input("have a nice day please come again!!!")
print("hotel")

#output

# l
# 10000456
# What is your name?hire
# Type of len = <class 'str'>
# What is your name?ji
# Type of len = <class 'int'>
# 170.25
# 2.0
# 8
# 59969536
# 2.67
# 2.679
# 2
# 4
# 6
# Enter your age: 65
# You have 1300 weeks left.
# You have 1300 weeks left.
# How much is the total bill? $1200
# How many no of people? 6
# How much is the tip percentage? 100
# Per person bill = $400.00