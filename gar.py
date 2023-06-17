class Employee:
    def __init__(self, name, position, status):
        self.name = name
        self.position = position
        self.status = status

    def calculate_salary(self):
        raise NotImplementedError("Subclass must implement abstract method")

class PermanentEmployee(Employee):
    def __init__(self, name, position, status):
        super().__init__(name, position, status)

    def calculate_salary(self):
        if self.position == "Manager":
            salary = 5000
        else:
            salary = 3000
        
        if self.status == "Married":
            salary += 500

        return salary

class ContractEmployee(Employee):
    def __init__(self, name, position, status):
        super().__init__(name, position, status)

    def calculate_salary(self):
        if self.position == "Manager":
            salary = 4000
        else:
            salary = 2000

        if self.status == "Married":
            salary += 300

        return salary

# Main program
def login():
    username = input("Username: ")
    password = input("Password: ")

    # Lakukan verifikasi login di sini, misalnya dengan database pengguna terdaftar

    # Jika login berhasil, kembali true
    return True

if login():
    name = input("Enter name: ")
    position = input("Enter position: ")
    status = input("Enter status: ")

    if position == "Permanent":
        employee = PermanentEmployee(name, position, status)
    elif position == "Contract":
        employee = ContractEmployee(name, position, status)
    else:
        print("Invalid position")
        exit()

    salary = employee.calculate_salary()
    print("Salary:", salary)
else:
    print("Login failed")
