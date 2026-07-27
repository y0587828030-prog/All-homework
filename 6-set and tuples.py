# Part 1 — Basics:
#1
tags = {'python', 'bash', 'git', 'python'}
print(len(tags))
#2
tags.add("linux")
print(len(tags))
#3
tags.discard('bash')
print(len(tags))

tags.discard('bbbb')
print(len(tags))

#4
a = {1, 2, 3}
b = {3, 4, 5} 

print(a | b)
print(a & b)
print(a - b | b-a)
print(a ^ b)

#5
print("git" in tags)

#6
point = (10, 20)
print(point)

print(point[0])
print(point[1])

#7
# point[0]=99
# print(point)

#8
rgb = (255, 128, 0)
r = rgb[0]
g = rgb[1]
b = rgb[2]

print(r,g,b)

#9
coords = (1, 2, 3, 2, 1)
#ספירה של ערך כמה פעים קיים בטאפל
print(coords.count(2))
# חיפוש לפי מספר באיזה אינדקס נמצא
print(coords.index(3))

#10
 # יש סדר # יש אפשרות לכפלויות# #ניתן לשינוי 
list = [1,2,3]
print(list)

#אין סדר #לא ניתן לכפלויות# ניתן לשיוי 
set = {1,2,3}
print(set)

# יש סדר # ניתן לכפלויות #לא ניתן לשינו
tuple = (1,2,3)
print(tuple)






















# recorded_runs = [
#     ("R001", 5.2), 
#     ("R002", 10.0), 
#     ("R001", 5.2), 
#     ("R003", 8.5), 
#     ("R002", 10.0)
# ]

# runs = set(recorded_runs)
# print(runs)

# runs_dict = dict(runs)
# print(runs_dict)

# print(runs_dict["R003"])

# #
# default_stats = {"total_runs": 0, "total_km": 0}

# runner_a = default_stats
# runner_b = default_stats

# runner_a["total_runs"] = 1

# print(runner_b["total_runs"])