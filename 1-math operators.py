# #part 1
# agent_name = "yehosh"
# mission_code = 123
# distance_to_target = 78.5
# mission_active = True

# print(agent_name, mission_code, distance_to_target)
# print(type(agent_name))
# print(type(mission_code))
# print(type(distance_to_target))
# print(type(mission_active))


# distance = distance_to_target * 2
# print(distance)

# fuel_usage = distance * 0.5
# print(fuel_usage)

# total_fuel = 200 - fuel_usage
# print(total_fuel)

# total = int(input("Enter total seconds: "))

# hours = total // 3600

# seconds_left = total % 3600

# minutes = seconds_left // 60

# final_seconds = seconds_left % 60

# print("Hours:", hours)
# print("Minutes:", minutes)
# print("Seconds:", final_seconds)

# distance_km = float(input("Enter distance km: "))

# distance_mel = distance_km * 0.621371
# print(distance_mel)


# old_name_of_agent = agent_name

# name_of_agent = input("Enter agent name: ")
# agent_name = name_of_agent

# print("new name: ",agent_name)
# print("old name: ",old_name_of_agent)

#part 2
print(bin(1))
print(bin(2))
print(bin(10))
print(bin(-10))

#
# חישוב 2 בחזקת 64 כדי למצוא את כמות המספרים האפשרית ב-8 בתים
total_numbers = 2 ** 64
print("Total numbers we can represent:", total_numbers)

num1 = 5
num2 = "5"

print(bin(num1))

#
val_true = True
val_false = False

bin_true = bin(val_true)
bin_false = bin(val_false)

print("Binary of True:", bin_true)
print("Binary of False:", bin_false)

if val_true > val_false:
    print ("True is larger than False!")

