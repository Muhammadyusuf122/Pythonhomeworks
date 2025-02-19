# Function to add a new employee record
def add_employee():
    # Get employee details from the user
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    salary = input("Enter Employee Salary: ")

    # Create a record string
    record = f"{emp_id}, {name}, {position}, {salary}\n"

    # Open the file in append mode and write the record
    with open("employees.txt", "a") as file:
        file.write(record)
    print("Employee record added successfully!")

# Function to display all employee records
def display_employees():
    try:
        # Open the file in read mode
        with open("employees.txt", "r") as file:
            records = file.readlines()

            # Check if the file is empty
            if not records:
                print("No employee records found.")
                return

            # Display all records
            print("\nEmployee Records:")
            print("-----------------")
            for record in records:
                print(record.strip())  # Remove extra newline characters
    except FileNotFoundError:
        print("No employee records found. Please add some records first.")

# Main program loop
def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if name == "main":
    main()