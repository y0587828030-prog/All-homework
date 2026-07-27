#Part 1 — Basics: list
#1
agents = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
print(agents)
#2
print(agents[0], agents[-1])
#3
print(agents[2])
#4
print(agents[1:4])
#5
agents.append("Foxtrot")
print(agents)
#6
agents.insert(2,"Zulu")
print(agents)
#7
agents.remove("Bravo")
print(agents)
#8
print(len(agents))
#9
scores = [42, 17, 95, 8, 61]
scores.sort()
print(scores)

print(max(scores))
print(min(scores))

#10
new_agent = agents.copy()
print(new_agent)

new_agent[0] = "jonson"
print(new_agent)
print(agents)

#part 2 
#1
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print("list after sort() ", numbers)


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
new_num = sorted(numbers)
print("New list from sorted():", new_num)
print(numbers)

#2
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

a.extend(b)
print(a)

#3
items = ['x', 'y', 'z', 'x', 'y', 'x']
print(items.count("x"))

items.remove('x')
items.remove('x')
items.remove('x')
print(items)

#4
data = [1, 2, 3, 4, 5]
print(data[0::2])

#5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])






# my_info= ["yehosh", "ishy", 2026-1999]
# print(my_info[1])

# nums = [10, 20, 30, 40]
# nums.append(50)
# nums.insert(2, 25)

# users = ["admin", "guest", "editor"]
# users.append("superuser")
# deleted_user = users.pop()
# print(deleted_user)

# runs= []
# runs.append(6)
# runs.append(8)
# runs.append(11)

# runs.insert(0,3)
# runs.remove(8)

# last_run = runs.pop()

# print(runs[0:2])