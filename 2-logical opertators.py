# # part 1
# #1
# is_online = True 
# has_access = False

# print(is_online and has_access)

# #2
# print(is_online or has_access)

# #3
# status = False
# print(not(status))

#4
# age = 20 
# has_id = True
# if age >= 18 and has_id:
#     print("welcome")

# #5
# level = 3
# print(1 <= level <= 5)

# #6
# a = 0
# b = "hello"
# c = ""


# print(bool(a))
# print(bool(b))
# print(bool(c))

# #7
# x = None
# y = 42

# print(x or y)

# #8
# username = ""
# default = "guest"

# username_final = username or default
# print(username_final)

# #9
# print(True and False or True)

#10
score = 75

print(score >= 60 and score <=100)


#part 2
#1
door_locked = False
has_key = False
admin_override = True

can_open = door_locked and (has_key or admin_override)

print(can_open)

#2
message = ""
backup_message = "No message found"

print(message or backup_message)

#3
x = None
print(x is None)

#4
a = 0
b = "ready"
c = 42

print(a or b or c)

#5
score = 85
print("pass" if score >= 60 else "fail")