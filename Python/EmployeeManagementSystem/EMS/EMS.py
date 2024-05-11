#!/usr/bin/env python3
""" Employee Management System Using Python - Sagar Developer """

from os import system
import re
import mysql.connector

""" making Connection """
con = mysql.connector.connect(
    host="localhost", user="root", password="", database="employee")

"""
make a regular expression
for validating an Email
"""
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# for validating an Phone Number
pattern = re.compile(r'0|\+254(7|8|9)?([7-9][0-9]{9})')


def Add_Employ():
    """
    Adds an employee record to the database.

    This function prompts the user to enter the employee's ID, name, email ID, phone number,
    address, post, and salary. It checks if the employee ID and name already exist in the
    database and prompts the user to try again if they do. It also validates the email ID and
    phone number using regular expressions. If the inputs are valid, the function inserts the
    employee details into the employee_data table in the database and prints a success message.

    Parameters:
    None

    Returns:
    None
    """
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    # checking If Employee Name is Exit Or Not
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ
    Email_Id = input("Enter Employee Email ID: ")
    if(re.fullmatch(regex, Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Phone_no = input("Enter Employee Phone No.: ")
    if(pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    # Instering Employee Details in
    # the Employee (empdata) Table
    sql = 'insert into employee_data values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    # Executing the sql Query
    c.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()

def check_employee_name(employee_name):
    """
    Check if an employee with the given name exists in the employee_data table.

    Parameters:
    - employee_name (str): The name of the employee to check.

    Returns:
    - bool: True if an employee with the given name exists, False otherwise.
    """
    # query to select all Rows from
    # employee(employee_data) table
    sql = 'select * from employee_data where Name=%s'

    """ making cursor buffered to make
    rowcount method work properly """
    c = con.cursor(buffered=True)
    data = (employee_name,)

    """ Execute the sql query """
    c.execute(sql, data)

    """ rowcount method to find number
     of rows with given values """
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

def check_employee(employee_id):

    sql = 'select * from employee_data where employee_id=%s'

    """
    Check if an employee with the given ID exists in the employee_data table.

    Parameters:
    - employee_id (int): The ID of the employee to check.

    Returns:
    - bool: True if an employee with the given ID exists, False otherwise.
    """
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Execute the sql query
    c.execute(sql, data)
    r = c.fetchall()  # or c.fetchone() if you expect only one result

    # rowcount method to find number
    # of rows with given values
    row_count = len(r)
    if row_count == 1:
        return True
    else:
        return False


def Display_Employ():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    """
    A function that displays all the details of all the employees in the employee_data table.

    This function executes a SQL query to select all the rows from the employee_data table,
    fetches all the details of the employees, and prints their Employee Id, Name, Email Id, Phone No,
    Address, Post, and Salary. It prompts the user to press any key to continue and then returns to the main menu.
    """
    # query to select all rows from Employee (employee_data) Table
    sql = 'select * from employee_data'
    c = con.cursor()

    # Executing the sql query
    c.execute(sql)

    # Fetching all details of all the Employees
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
    press = input("Press Any key To Continue..")
    menu()

def Update_Employ():
    """
    A function that updates an employee's information in the employee_data table.

    This function prompts the user for the employee's ID, email, phone number, and address.
    It validates the email and phone number inputs, updates the employee's details in the database,
    and commits the changes.

    Parameters:
    None

    Returns:
    None
    """
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Email_Id = input("Enter Employee Email ID: ")
        if(re.fullmatch(regex, Email_Id)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Phone_no = input("Enter Employee Phone No.: ")
        if(pattern.match(Phone_no)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Address = input("Enter Employee Address: ")
        # Updating Employee details in employee_data Table
        sql = 'UPDATE employee_data set Email_Id = %s, Phone_no = %s, Address = %s where Id = %s'
        data = (Email_Id, Phone_no, Address, Id)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the table
        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        menu()

def Promote_Employ():
    print("{:>60}".format("-->> Promote Employee Record <<--\n"))
    """
    Promotes an employee by increasing their salary in the employee_data table.

    The function prompts the user to enter an employee ID. If the employee exists in the table,
    it asks for the amount to increase the salary. It then fetches the salary of the employee with the given ID,
    calculates the new salary, updates the salary in the table, and commits the changes.
    If the employee does not exist, it prompts the user to try again.

    Parameters:
    None

    Returns:
    None
    """
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount  = int(input("Enter Increase Salary: "))
        #query to fetch salary of Employee with given data
        sql = 'select * from employee_data where employee_id=%s'
        data = (Id,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql, data)

        #fetching salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount

        #query to update salary of Employee with given id
        sql = 'select * from employee_data where employee_id=%s'
        d = (t, Id)

        #executing the sql query
        c.execute(sql, d)

        #commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        press = input("Press Any key To Continue..")
        menu()

def Remove_Employ():
    """
    Removes an employee record from the employee_data table.

    This function prompts the user to enter an employee ID and checks if the
    employee exists in the employee_data table. If the employee exists, it deletes
    the employee record from the table. If the employee does not exist, it prompts
    the user to try again and returns to the main menu.

    Parameters:
    None

    Returns:
    None
    """
    print("{:>60}".format("-->> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        # query to delete Employee from employee_data table
        sql = 'DELETE FROM employee_data WHERE employee_id=%s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # fetch any remaining result to consume it
        c.fetchall()

        # commit() method to make changes in the employee_data table
        con.commit()
        print("Employee Removed")
        press = input("Press Any key To Continue..")
        menu()

def Search_Employ():
    """
    Searches for an employee record by their employee ID.

    This function prompts the user to enter an employee ID and checks if the
    employee exists in the employee_data table. If the employee exists, it fetches all
    the details of the employee and displays them. If the employee does not exist, it
    prompts the user to try again and returns to the main menu.

    Parameters:
    None

    Returns:
    None
    """
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    """checking If Employee Id is Exit Or Not """
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        """ query to search Employee from employee_data table """
        sql = 'select * from employee_data where employee_id=%s'
        data = (Id,)
        c = con.cursor()

        """ executing the sql query """
        c.execute(sql, data)


        """ fetching all details of all the employee """
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
        press = input("Press Any key To Continue..")
        menu()

""" Menu function to display menu """
def menu():
    """
    Displays a menu for the Employee Management System and prompts the user to choose an option.

    This function clears the screen and displays a menu with the following options:
    1. Add Employee
    2. Display Employee Record
    3. Update Employee Record
    4. Promote Employee Record
    5. Remove Employee Record
    6. Search Employee Record
    7. Exit

    The user is prompted to enter their choice and the corresponding action is performed.

    Parameters:
    None

    Returns:
    None
    """
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        Promote_Employ()
    elif ch == 5:
        system("cls")
        Remove_Employ()
    elif ch == 6:
        system("cls")
        Search_Employ()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()


""" Calling menu function """
menu()