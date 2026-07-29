## Inheritance
#1
class Athlete:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.")

class Swimmer(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age)

swin = Swimmer("tom", 22)
swin.introduce()

#2
class Athlete:
    def __init__(self,name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport

    def describe(self):
        print(f"{self.name} competes in {self.sport}.")

class Runner(Athlete):
    def __init__(self, name, age ):
        super().__init__(name, age, sport="running")

run1 = Runner("bob", 25)
run1.describe()

#3
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete")

class Cyclist(Athlete):
    def __init__(self, name, age, bike_brand):
        super().__init__(name, age)
        self.bike_brand =bike_brand

    def describe_gear(self):
        print(f"Cyclist {self.name} rides a {self.bike_brand}.")

cyclist1 = Cyclist("Mike", 30, "Trek")
cyclist1.introduce()
cyclist1.describe_gear()

#4
class Athlete:
    def __init__(self, name, country):
        self.name = name
        self.country =country

    def greet(self):
        print(f"{self.name} represents {self.country}")

class Swimmer(Athlete):
    def __init__(self, name, country, stroke_style):
        super().__init__(name, country)
        self.stroke_style = stroke_style

class Runner(Athlete):
    def __init__(self, name, country, best_distance):
        super().__init__(name, country) 
        self.best_distance = best_distance

class Cyclist(Athlete):
    def __init__(self, name, country, race_type):
        super().__init__(name, country)
        self.race_type = race_type

swim =  Swimmer("Lior", "Israel", "freestyle") 
swim.greet()  
run =   Runner("Avi", "Kenya", "marathon") 
run.greet()
cycli = Cyclist("Jan", "France", "road")
cycli.greet()

#5
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age =age

    def warm_up(self):
        print(f"{self.name} is warming up.")

class Gymnast(Athlete):
    def __init__(self, name, age, apparatus):
        super().__init__(name, age)
        self.apparatus = apparatus

    def compete(self):
        print(f"{self.name} competes on the {self.apparatus} ")

class Swimmer(Athlete):
    def __init__(self, name, age, stroke):
        super().__init__(name, age)
        self.stroke = stroke

    def compete(self):
        print(f"{self.name} competes in {self.stroke} ")

gym = Gymnast("Ana", 19, "rings")
gym.warm_up()
gym.compete()

swim1 = Swimmer("Ben", 21, "butterfly")
swim1.warm_up()
swim1.compete()


#6
class Athlete:
    def __init__(self, name, age, years_active):
        self.name = name
        self.age = age
        self. years_active =  years_active

    def experience(self):
        print(f"{self.name} has been active for {self.years_active} years.")
        
class TeamSportPlayer(Athlete):
    def __init__(self, name, age, years_active, team_name):
        super().__init__(name, age, years_active)

        self.team_name = team_name

    def team_info(self):
        print(f"{self.name} plays for {self.team_name}.")

tem = TeamSportPlayer("Gal", 28, 10, "Maccabi")
tem.team_info()
tem.experience()

#7
class Athlete:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport
        self.personal_best = None

    def set_record(self, value):
        self.value = value
        self.personal_best = value
        print(f"new record: {value}")

    def has_record(self):
        return self.personal_best != None

class Sprinter(Athlete):
    def __init__(self, name):
        super().__init__(name, sport= "100m Sprint")


sprin = Sprinter("Usain")
sprin.set_record(10.8)
print(sprin.has_record())

#8
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sessions_completed = 0

    def train(self):
        self.sessions_completed += 1

    def sessions_needed(self, target):
        need = target -  self.sessions_completed
        if need > 0:
            return need
        elif need == 0:
            return f"You have arrived at your destination"
        else:
            over = self.sessions_completed - target
            return f"{over}- Number of extra workouts."            


class Triathlete(Athlete):
    def __init__(self, name, age, discipline):
        super().__init__(name, age)
        self.discipline = discipline

    def Triathlete(self):
        print(f"Triathlete {self.name}, age {self.age}, discipline: {self.discipline}")

tri = Triathlete("Dan", 26, "cycling")
tri.train()
tri.train()
tri.train()
tri.train()
tri.train()

print(tri.sessions_needed(10))

print(f"{tri.sessions_completed} sessions completed. {tri.sessions_needed(10)} more needed.")


tri.Triathlete()

#9
class Athlete:
    def __init__(self,name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def player_card(self):
        print(f" name: {self.name} | age: {self.age} | position {self.position}") 

class BasketballPlayer(Athlete):
    def __init__(self, name, age, position, jersey_number):
        super().__init__(name, age, position)
        self.jersey_number = jersey_number

    def full_profile(self):
        self.player_card()
        print(f"Jersey: #{self.jersey_number}")

playr1= BasketballPlayer("Mia", 24, "guard", 7)
playr1.full_profile()

playr2= BasketballPlayer("bob", 35, "guard", 8)
playr2.full_profile()

playr3= BasketballPlayer("mase", 42, "guard", 10)
playr3.full_profile()

#10
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name}")

class Athlete(Person):
    def __init__(self, name, age, sport):
        super().__init__(name, age)
        self.sport = sport

    def train(self):
        print(f"{self.name} is training for {self.sport}.")

class ProfessionalAthlete(Athlete):
    def __init__(self, name, age, sport,sponsor):
        super().__init__(name, age, sport)
        self.sponsor = sponsor

    def sponsor_info(self):
        print(f"{self.name} is sponsored by {self.sponsor}.") 

pro = ProfessionalAthlete("Ronaldo", 39, "football", "Nike")
pro.greet()
pro.train()
pro.sponsor_info()


        



        





        




#practice
# class Animal:
#     def  breathe(self):
#         print("Breathing")

# class Dog(Animal):
#     def bark (self):
#         print("woof")

# dog1= Dog()
# dog1.breathe()
# dog1.bark()

# ##
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)

#         self.age = age

#     def make_sound(self):
#         print("meow")

# cat1 =Cat("mitzi", 3)
# print(cat1.name, cat1.age)

# cat1.make_sound()

# ##
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary

#     def work(self):
#         print(f"{self.name} is doing general work.") 


# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)

#         self.programming_language =programming_language

#     def write_code(self):
#         print(f"{self.name} is writing code in {self.programming_language}.") 

# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary) 
#         self.team_size =team_size

#     def work(self):
#         print(f"{self.name} i am menager.") 

#     def hold_meeting(self):
#         print(f"{self.name} is holding a meeting with {self.team_size} employees.") 


# Developer1 = Developer("yehosh", 35000, "python")
# Manager1 = Manager("shi", 12500, 5)

# Developer1.work()
# Manager1.work()

# Developer1.write_code()
# Manager1.hold_meeting()


        

