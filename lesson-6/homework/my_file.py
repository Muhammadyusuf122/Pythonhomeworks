
import os


def create_file():
    if not os.path.exists(r"file path"):#txt file qayerda create bo'lishini xohlasangiz o'shayerni pathini bering
        with open("employees.txt", "w") as file:
            pass 

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = str(input("Enter Employee Name: "))
    position = str(input("Enter Employee Position: "))
    salary = int(input("Enter Employee Salary: "))

    with open("employees.txt", mode="w") as file:
        file.write(f"{emp_id}, {name}, {position}, {salary}\n") 
        print("Employee record added successfully.")

def view_employees():
    pass


def search_employee():
    pass

def update_employee():
   pass

def delete_employee():
    pass


def main():
    create_file()

    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee")
        print("2. View all employee")
        print("3. Search for an employee by Employee-ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if name == "main":
    main()

 
    