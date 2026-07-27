## Part 1 — Basics: dict CRUD
#1
agent = {'name': 'Alpha', 'level': 3, 'active': True}
print(agent)
#2
print(agent["name"])
#3
current_level = agent.get("level")
print(current_level)
#4
agent['score']=95
print(agent)
#5
agent['level'] = 5
print(agent)
#6
del agent ['active']
print(agent)
#7
print(agent.keys())
print(agent.values())
print(agent.items())
#8
print('score' in agent)
#9
scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
highes_agent = max(scores, key=scores.get)
print(highes_agent)
#10
scores_new = scores.copy()
del scores['Alpha']
print(scores_new)
print(scores)










# My_details = {
# "name" : "yehosh",
# "age" : 26,
# "adrs": "yeahi",
# "run km" : [3,5,9],
# "favorite_animal" : []

# }


# My_details["age"] = My_details["age"]+1
# My_details["name"]= My_details["name"].upper()
# del My_details["adrs"]
# print(My_details)

# print("age" in My_details)
# print("adrs" in My_details)


# current_name = My_details.get("name")
# print(current_name)

# print(My_details.values())

# current_age = My_details.get("age")
# print(current_age)

# print(f"my name is {current_name} ans is age is {current_age}")

# print(My_details)

###
# balcony_plants = {
# "rosemary": 1 ,
# "sage" : 2 , 
# "myrtle": 3
# }

# balcony_plants["mint"] = 4
# current_mint = balcony_plants.get("mint")
# print(current_mint)
# print(balcony_plants)

# balcony_plants["myrtle"] = balcony_plants["myrtle"] +2
# balcony_plants["sage"] = balcony_plants["sage"] +2
# balcony_plants["rosemary"] = balcony_plants["rosemary"] +2
# balcony_plants["mint"] = balcony_plants["mint"]+2

# print(balcony_plants)

# del balcony_plants ["mint"]
# print("mint" in balcony_plants)
# print(balcony_plants)

# print(balcony_plants.items())



