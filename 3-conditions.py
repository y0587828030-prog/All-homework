# #part 1 Basics: if, else, elif
# #1

# age = int(input("How old are you?"))
# if age >= 18:
#     print("Can enter")
# else:
#     print("Cannot enter")

# #2
# temperature = 38.2
# if temperature > 37.5:
#     print("High temperature")
# else:
#     print("Normal temperature")

# #3
# num = int(input("give a number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# #4
# battery = 15
# is_charging = True

# if battery < 20 and is_charging:
#     print("Low battery, charging now")
# elif battery < 20 and not is_charging:
#     print("Low battery, connect charger")
# else:
#     print("Battery OK")

# #5
# password = input("give a password: ")
# if password == "python123":
#     print("Access approved")
# else:
#     print("Access denied")

# #6
# score = 72
# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Good")
# elif score >= 60:
#     print("Pass")
# else:
#     print("Fail")

# #7
# num1 = int(input("give a numer 1: "))
# num2 = int(input("give a numer 2: "))
# if num1 > num2:
#     print( "First is bigger")
# elif num2 > num1:
#     print( "Second is bigger")
# else:
#     print("Equal")


# #8
# fuel = int(input("gieve a fuel: "))
# distance = int(input("gieve a distance: "))
# good_fuel = fuel - distance
# if good_fuel >= 10:
#     print("Enough fuel with reserve")
# elif good_fuel < 10 and good_fuel >=0:
#     print("Enough fuel, low reserve")
# else:
#     print("Not enough fuel")

#9
username = input("give a name: ")
if username == "":
    print("Guest user")
else:
    print(f"hellp", username)

#10
hour = 21
if hour < 0 or hour > 23:
    print("Invalid hour")
elif hour < 12:
    print("Morning")
elif hour < 18:
    print("Afternoon")
else:
    print("Evening")








# age = 20
# height = 165

# if age >= 10 and  height >= 110:
#     print("You can go on")
# else:
#     print("You cannot go on")


# temperature = 35

# weather_status = "hot" if temperature > 30  else "cold"
# print(weather_status)


# income = 25000
# credit_score = 950
# is_criminal = False

# if is_criminal:
#     print("Loan Denied: Criminal record")
# elif  income > 10000 and credit_score > 700:
#     print("Loan Approved: Excellent profile")
# elif  income > 10000 or credit_score > 700:
#     print("Loan Approved: Good profile")
# else:
#     print("Loan Denied: Insufficient criteria")
