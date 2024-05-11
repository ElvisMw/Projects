#!/usr/bin/env python3

from os import system
import re
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="angel", database="employee")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

pattern = re.compile("0|+254(7|8|9)?([7-9][0-9]{9})")

def Add_Employee():
    print("\nAdd Employee Record\n")
    id = input(f"Enter Employee ID: ")

    if (check_employee(id) == True):
        print(f"Employee ID {id} already exists\nTry Again ...")
        press = input(f"Press any key to continue ...")
        Add_Employee()
    Name = input(f"Enter Employee Name: ")

    if (check_employee_name(Name) == True):
        print(f"Employee Name {Name} already exists\nTry Again ...")
        press = input(f"Press any key to continue ...")
        Add_Employee()

    Email_Id = input(f"Enter Employee Email ID: ")
    if (re.fullmatch(regex, Email_Id)):
        print(f"Valid email address: {Email_Id}")
    else:
        print(f"Invalid email address: {Email_Id}")
        Add_Employee()

    Mobile_Number = input(f"Enter Employee Mobile Number: ")
    if (re.fullmatch(pattern, Mobile_Number)):
        print(f"Valid Mobile Number: {Mobile_Number}")
    else:
        print(f"Invalid Mobile Number: {Mobile_Number}")
        Add_Employee()

    Address = input(f"Enter Employee Address: ")
    Post = input(f"Enter Employee Post: ")
    Salary = input(f"Enter Employee Salary: ")
    data = (id, Name, Email_Id, Mobile_Number, Address, Post, Salary)

    sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s)"
    c = con.cursor()

    c.execute(sql, data)

    con.commit()

    print("\nEmployee Record Added Successfully")
    press = input(f"Press any key to continue ...")
    menu()

def check_employee_name(employee_name):

    sql = "SELECT * FROM empdata WHERE Name=%s"

    c = con.cursor(buffered=True)
    data = (employee_name,)

    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def Display_Employee():
    print(f"\nDisplay Employee Record\n")

    sql = "SELECT * FROM empdata"

    c = con.cursor()

    c.execute(sql)

    r = c.fetchall()

    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")

    press = input(f"Press any key to continue ...")
    menu()

def Update_Employee():
    print(f"\nUpdate Employee Record\n")

    id = input(f"Enter Employee ID: ")

    if (check_employee(id) == False):
        print(f"Employee ID {id} does not exists\nTry Again ...")