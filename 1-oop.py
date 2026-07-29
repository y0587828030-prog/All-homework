# oop
#1
class MenuItem:
    name = "Espresso"
    price = 3.5

    def describe(self):
        print(f" item: {self.name} | price: ${self.price}")

a= MenuItem()
a.describe()

#2
class Customer:
    def __init__(self, name, favorite_drink ):
        self.name =  name
        self.favorite_drink = favorite_drink

    def greet(self):
        print(f"Hi! I am {self.name} and I would like a {self.favorite_drink}.")

cousumer = Customer("jio", "coffe")
cousumer.greet()

#3
class Customer:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"Item: {self.name} | Price: ${self.price}") 

customer1 = Customer("Latte",4.5)
customer1.describe()
customer2 = Customer("Croissant",2.0)
customer2.describe()
customer3 = Customer("Cold Brew",5.0)
customer3.describe()

#4
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def can_afford(self, price):
        self.price =price
        if price <= self.balance:
            return True
        else:
            return False

customer = Customer("Bob", 10.0)
print(customer.can_afford(8.0)) 
print(customer.can_afford(12.0)) 

#5
class MenuItem:
    def __init__(self, name,price, in_stock):
        self.name = name
        self.price = price
        self.in_stock  = in_stock

    def sell(self):
        self.in_stock = False

    def restock(self):
        self.in_stock = True

    def status(self):
        if self.in_stock == True:
           print(f'{self.name} is in stock')
        else:
            print(f"{self.name} is sold out")

item = MenuItem("Muffin", 2.5, True)
item.status()
item.sell()
item.status()
item.restock()
item.status()

#6
class CoffeeShop:
    def __init__(self, name, city, capacity):
        self.name = str(name)
        self.city =str(city)
        self.capacity = int(capacity)

    def open_shop(self):
        print(f"{self.name} is now open in {self.city}! Capacity: {self.capacity} seats.")
        
    def close_shop(self):
        print(f"{self.name} is now closed. See you tomorrow!")

customer = CoffeeShop("Brew House", "Tel Aviv", 40)
customer.open_shop()
customer.close_shop()

#7
class MenuItem:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
        self.order_count = 0

    def order(self):
        self.order_count += 1
        print(f"{self.name} ordered. Total orders: {self.order_count}") 
        
claint = MenuItem("Cappuccino", 4.0)  
claint.order()
claint.order()
claint.order()

#8

class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items

    def item_count(self):
        return len(self.items)

    def print_order(self):
        print(f"Order for: {self.customer_name}")
        for _ in self.items:
            print(f"-{_}")

custumar = Order("Dana", ["Latte", "Croissant", "OJ"])
custumar.item_count()
custumar.print_order()

#9
class Barista:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.drinks_made = 0

    def make_drink(self, drink_name):
        self.drink_name = drink_name
        print(f"{self.name} made a {self.drink_name}")
        self.drinks_made += 1

    def is_specialty(self, drink_name):
        self.drink_name = drink_name
        if self.drink_name == self.specialty:
            return True
        else:
            return False

    def shift_summary(self):
        print(f"{self.name} made {self.drinks_made} drinks today.")

claint = Barista("Yossi", "Espresso")
claint.make_drink("Espresso")
claint.make_drink("coffe")
claint.make_drink("tae")
claint.make_drink("latte")

print(claint.is_specialty("Espresso"))

claint.shift_summary()

#10
class Receipt:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate
        self.items = []

    def add_item(self, name, price):
        self.items.append((name,price))

    def subtotal(self):
        total_sum = 0
        for item in self.items:
            total_sum += item[1]
        return total_sum

    def tax_amount(self):
        total = self.subtotal()
        tax_total = total * self.tax_rate
        return tax_total

   
    def total(self):
        return self.subtotal() * 100/100 + self.tax_amount()

    def print_receipt(self): 
       for item in self.items:
            name = item[0]
            price = item[1]
            print(f"- {name} ${price}")

       print(f"Subtotal: ${self.subtotal()}")
       print(f"Tax ({int(self.tax_rate * 100)}%)  ${self.tax_amount()}")
       print(f"Total: ${self.total()}")

receipt = Receipt(0.17)
receipt.add_item("Latte", 4.5)
receipt.add_item("Croissant", 2.0)
receipt.add_item("Water", 1.5) 

receipt.print_receipt()
        
















# class Dog:
#     legs = 4

# dog1 = Dog()
# dog2 = Dog()

# print(dog1.legs)

# class Student:
#     name = "yehosh"
#     study_class = 1
#     grade_average =95 

#     def say_grades(self):
#         print(f"my name is: {self.name} in class {self.study_class} the grade average is: {self.grade_average}  ")

# student1 = Student()
# student1.say_grades()

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def say_name(self):
#         print(self.name)

# bob = Person("bob")
# bob.say_name()

# alice =  Person("alice")
# alice.say_name()

# class Teacher:
#     def __init__(self, name, age, years_of_experience):
#         self.name = name
#         self.age = age
#         self.years_of_experience = years_of_experience

#     def print_details(self):
#         print(f" me name is {self.name} I am {self.age} years old I have {self.years_of_experience} years of experience.")


# class Student:
#     def __init__(self, name, age, list_of_classes):
#         self.name = name
#         self.age = age
#         self.list_of_classes = list_of_classes

#     def say_name(self):
#        print(f" my name is {self.name}")

#     def print_details(self):
#         print(f" I am {self.age} years old I have - i am larn {self.list_of_classes}")

# teacher1 = Teacher("yssi", 35, 15)
# teacher1.print_details()

# teacher2 = Teacher("bob", 45, 10)
# teacher2.print_details()

# student1 = Student("yehosh", 26, ["python"])
# student1.say_name()
# student1.print_details()

# student2 = Student("jon", 35, ["elctronic"])
# student2.say_name()
# student2.print_details()



# class Task:
#     def __init__(self, title, category):
#         self.title = title
#         self.category = category

#         self.is_completed = False
#         self.due_dat = None

#     def complete_task(self):
#         self.is_completed = True

#     def set_due_date(self, date):
#         self.due_dat = date

#     def print_task_info(self):
#         print(f"{self.title} | {self.category} | {self.is_completed} | {self.due_dat}")

# a= Task("python" , "larn")
# a.complete_task()
# a.set_due_date("27.07.26")
# a.print_task_info()

# b= Task("run", "spotr")
# b.print_task_info()



        



