import mysql.connector
import bcrypt

# Function to establish a connection to a specific database
def get_connection(database_name):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Azim@2002",  # Replace with your MySQL root password
        database=database_name
    )
    return connection

# Function to hash a password
def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

# Function to store employee data
def store_employee_data():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")  # You can add password hashing
    position = input("Enter Position: ")
    department = input("Enter Department: ")
    joining_date = input("Enter Joining Date (YYYY-MM-DD): ")

    # Hash the password before storing it
    hashed_password = hash_password(password)

    conn = get_connection("Employees")  # Connect to Employees database
    cursor = conn.cursor()

    query = "INSERT INTO Employees (FirstName, LastName, Email, Password, Position, Department, DateOfJoining) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, email, hashed_password, position, department, joining_date)
    cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

    print("Employee data inserted successfully.")

# Function to store employer data
def store_employer_data():
    company_name = input("Enter Company Name: ")
    contact_person = input("Enter Contact Person Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")  # You can add password hashing
    company_size = input("Enter Company Size: ")
    industry_type = input("Enter Industry Type: ")
    registration_date = input("Enter Registration Date (YYYY-MM-DD): ")

    # Hash the password before storing it
    hashed_password = hash_password(password)

    conn = get_connection("Employers")  # Connect to Employers database
    cursor = conn.cursor()

    query = "INSERT INTO Employers (CompanyName, ContactPerson, Email, Password, CompanySize, IndustryType, DateOfRegistration) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (company_name, contact_person, email, hashed_password, company_size, industry_type, registration_date)
    cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

    print("Employer data inserted successfully.")

# Function to retrieve all employees
def retrieve_employee_data():
    conn = get_connection("Employees")  # Connect to Employees database
    cursor = conn.cursor()

    query = "SELECT * FROM Employees"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Email: {row[3]}, Position: {row[4]}, Department: {row[5]}, Joining Date: {row[6]}")

    cursor.close()
    conn.close()

# Function to retrieve all employers
def retrieve_employer_data():
    conn = get_connection("Employers")  # Connect to Employers database
    cursor = conn.cursor()

    query = "SELECT * FROM Employers"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, Company Name: {row[1]}, Contact Person: {row[2]}, Email: {row[3]}, Company Size: {row[4]}, Industry Type: {row[5]}, Registration Date: {row[6]}")

    cursor.close()
    conn.close()

# Function to authenticate user
def authenticate_user(first_name, last_name, password):
    conn = get_connection("Employees")
    if conn:
        cursor = conn.cursor()
        query = "SELECT Password FROM Employees WHERE FirstName = %s AND LastName = %s"
        cursor.execute(query, (first_name, last_name))

        row = cursor.fetchone()
        
        if row:
            stored_password = row[0]
            print(f"Stored Password Hash: {stored_password}")  # Debug print

            # Check if the entered password matches the stored hashed password
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                return True  # Authentication successful
            else:
                print("Password mismatch")  # Debug print
        else:
            print("No user found with these credentials")  # Debug print

        cursor.close()
        conn.close()
    return False  # Authentication failed

# Menu-based script
if __name__ == "__main__":
    while True:
        print("\nMENU")
        print("1. Insert Employee Data")
        print("2. Insert Employer Data")
        print("3. Retrieve Employee Data")
        print("4. Retrieve Employer Data")
        print("5. Authenticate User")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            store_employee_data()
        elif choice == "2":
            store_employer_data()
        elif choice == "3":
            retrieve_employee_data()
        elif choice == "4":
            retrieve_employer_data()
        elif choice == "5":
            first_name = input("Enter First Name for authentication: ")
            last_name = input("Enter Last Name for authentication: ")
            password = input("Enter Password for authentication: ")
            if authenticate_user(first_name, last_name, password):
                print("Authentication successful.")
            else:
                print("Invalid credentials.")
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
