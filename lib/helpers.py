from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input('Enter the name of the employee: ')
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f'Employee {name} not found')


def find_employee_by_id():
    id = input('Enter the id of the employee: ')
    employee = Employee.find_by_id(id)
    print(employee) if employee else print(f'Employee {id} not found')


def create_employee():
    name = input('Enter the name of the employee: ')
    job_title = input("Enter the employee's Job Title: ")
    department_id = int(input("Enter the employee's Department ID: "))

    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success', employee)
    except Exception as exc:
        print(f'Error creating employee:',exc)


def update_employee():
    id = int(input('Enter the id of the employee to be updated: '))
    if employee := Employee.find_by_id(id):
        try:
            name = input('Enter the new name: ')
            job_title = input('Enter the new Job title: ')
            department_id = int(input('Enter the new Department id: '))
            print('Previous employee details\n', employee)
            employee.name = name
            employee.job_title = job_title
            employee.department_id = department_id
            employee.update()
            print('Updated employee details\n', employee)
        except Exception as exc:
            print("Error updating employee: ", exc)


def delete_employee():
    id = input('Enter the ID of the employee to be deleted: ')
    if employee := Employee.find_by_id(id):
        employee.delete()
        print('The following employee has been deleted\n', employee)
    else:
        print(f'Employee {id} not found')


def list_department_employees():
    id = input('Enter the department id: ')
    department = Department.find_by_id(id)

    if department:
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f'Department {id} not found')