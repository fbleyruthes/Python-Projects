#Electronic Timekeeping System

#Libraries
import os
from datetime import datetime, timedelta

#Variables
b = True

#Classes
class Company:
    def __init__(self, **dc):
        self.name = dc['name']
        self.identification = dc['EIN']
        self.__employees = []
        self.__projects = []
        if 'employees' in dc:
            for i in dc['employees']:
                self.__employees.append(i)
        if 'projects' in dc:
            for i in dc['projects']:
                self.__projects.append(i)
    def get_employees(self):
        return self.__employees
    def get_projects(self):
        return self.__projects
    
class Employee:
    def __init__(self, **de):
        self.name = de['name']
        self.jobRole = de['role']
        self.__hourCost = de['cost']
        self.__id = de['id']
        self.__password = de['password']
        self.__age = de['age']
        self.__address = de['add']
    def get_id(self):
        return self.__id
    def get_age(self):
        return self.__age
    def get_address(self):
        return self.__address
    def get_password(self):
        return self.__password
    def get_hourCost(self):
        return self.__hourCost
    
class Project:
    def __init__(self, **dp):
        self.__name = dp['name']
        self.head = dp['head']
        self.startDate = dp['startDate']
        self.endDate = dp.pop('endDate','Ongoing Project')
    def get_projectName(self):
        return self.__name
    
#Objects
employee1 = Employee(name = 'Leandro Silva', role = 'Web Developer', cost = 70, id = '444', age = '42', add = '123 Main Street, Anytown, USA', password = '4322')
employee2 = Employee(name = 'Janete Nascimento', role = 'Product Manager', cost = 80, id = '555', age = '35', add = '566 Main Street, Anytown, USA', password = '4511')
employee3 = Employee(name = 'Fernanda Ferreira', role = 'Designer', cost = 50, id = '888', age = '25', add = '789 Main Street, Anytown, USA', password = '5678')

project1 = Project(name = 'Prime Video', head = employee2.name, startDate = '01/02/2023')
project2 = Project(name = 'Kindle', head = 'Karina Costa', startDate = '01/03/2015', endDate = '01/08/2016')
project3 = Project(name = 'Amazon Music', head = 'Emiliano Pereira', startDate = '10/07/2021')

company = Company(name = 'Amazon', EIN = '12-3456789', employees = [employee1, employee2, employee3], projects = [project1, project2, project3]) 

#Main program
print("Check-in\n")

#The employee must inform his/her ID
while (b):
    id = str(input("ID: "))
    if ((id != employee1.get_id()) and (id != employee2.get_id()) and (id != employee3.get_id())):
        os.system('cls')
        print("ID not found. Please, type a valid ID.")
    else:
        b = False
b = True
os.system('cls')

#Password to check-in
while (b):
    if (id == employee1.get_id()):
        password = str(input("Password: "))
        if ((password != employee1.get_password())):
            os.system('cls')
            print("Invalid password. Please, try again.")
        else:
            b = False
    elif (id == employee2.get_id()):
        password = str(input("Password: "))
        if ((password != employee2.get_password())):
            os.system('cls')
            print("Invalid password. Please, try again.")
        else:
            b = False
    elif (id == employee3.get_id()):
        password = str(input("Password: "))
        if ((password != employee3.get_password())):
            os.system('cls')
            print("Invalid password. Please, try again.")
        else:
            b = False
b = True
os.system('cls')

#Project selection
while (b):
    projectChoice = str(input("Select the project you are working at: "))
    if ((projectChoice != project1.get_projectName()) and (projectChoice != project2.get_projectName()) and (projectChoice != project3.get_projectName())):
        os.system('cls')
        print("Invalid project name. Try again.")
    else:
        b = False

#Check-in message
if (id == employee1.get_id()):
    print("Check-in done at {}, {}.".format(datetime.now().strftime("%H:%M:%S"), employee1.name))
elif (id == employee2.get_id()):
    print("Check-in done at {}, {}.".format(datetime.now().strftime("%H:%M:%S"), employee2.name))
elif (id == employee3.get_id()):
    print("Check-in done at {}, {}.".format(datetime.now().strftime("%H:%M:%S"), employee3.name))
ckin = datetime.now()
b = True

#Password to Check-out
while (b):
    if (id == employee1.get_id()):
        password = str(input("Type your password again to check-out: "))
        if ((password != employee1.get_password())):
            os.system('cls')
            print("Invalid password. Please, try again.")
        else:
            b = False
    elif (id == employee2.get_id()):
        password = str(input("Type your password again to check-out: "))
        if ((password != employee2.get_password())):
            os.system('cls')
            print("Invalid password. Please, try again.")
        else:
            b = False
    elif (id == employee3.get_id()):
        password = str(input("Type your password again to check-out: "))
        if ((password != employee3.get_password())):
            os.system('cls')
            print("Invalid password. Please, try again.")
        else:
            b = False
os.system('cls')

#Check-out message
if (id == employee1.get_id()):
    print("Check-out done at {}, {}.".format(datetime.now().strftime("%H:%M:%S"), employee1.name))
elif (id == employee2.get_id()):
    print("Check-out done at {}, {}.".format(datetime.now().strftime("%H:%M:%S"), employee2.name))
elif (id == employee3.get_id()):
    print("Check-out done at {}, {}.".format(datetime.now().strftime("%H:%M:%S"), employee3.name))
ckout = datetime.now()
deltaT = ckout - ckin

#Timekeeping record message
print("Follow the timekeeping record:")

if (id == employee1.get_id()):
    print("{}, {} at {}, worked on the project {} from {} to {} on {}. His/Her worked {} hours and it will cost {} dollars for de EIN: {}.".format(employee1.name, employee1.jobRole, company.name, projectChoice, ckin.strftime("%H:%M:%S"), ckout.strftime("%H:%M:%S"), datetime.now().strftime("%d/%m/%Y"), deltaT.total_seconds() / 3600, round((deltaT.total_seconds() / 3600)*employee1.get_hourCost(), 2), company.identification))
elif (id == employee2.get_id()):
    print("{}, {} at {}, worked on the project {} from {} to {} on {}. His/Her worked {} hours and it will cost {} dollars for de EIN: {}.".format(employee2.name, employee2.jobRole, company.name, projectChoice, ckin.strftime("%H:%M:%S"), ckout.strftime("%H:%M:%S"), datetime.now().strftime("%d/%m/%Y"), deltaT.total_seconds() / 3600, round((deltaT.total_seconds() / 3600)*employee1.get_hourCost(), 2), company.identification))
elif (id == employee3.get_id()):
    print("{}, {} at {}, worked on the project {} from {} to {} on {}. His/Her worked {} hours and it will cost {} dollars for de EIN: {}.".format(employee3.name, employee3.jobRole, company.name, projectChoice, ckin.strftime("%H:%M:%S"), ckout.strftime("%H:%M:%S"), datetime.now().strftime("%d/%m/%Y"), deltaT.total_seconds() / 3600, round((deltaT.total_seconds() / 3600)*employee1.get_hourCost(), 2), company.identification))




