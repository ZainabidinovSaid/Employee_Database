from employee_class import Employee
from employee_DAO import EmployeeDAO


if __name__ == "__main__":
    dao = EmployeeDAO()

    while True:
        action = int(input("""
        <Employee database>
        1. Add employee
        2. Delete employee by id
        3. See all employees
        4. Get employee by id
        5. Update employee information by id
        6. Delete all employees
        7. Exit
        Choose the action: """))

        if action == 1:
            try:
                emp_info = input("Enter employee's info (id, name, position, salary, hire date YYYY-MM-DD): ")
                emp_id, name, position, salary, hire_date = emp_info.split(", ")
                emp = Employee(int(emp_id), name, position, float(salary), hire_date)
                dao.insert(emp)
            except Exception as e:
                print(f"Oops, Error: {e}")

        elif action == 2:
            emp_id = int(input("Enter employee id to delete: "))
            dao.delete(emp_id)
            print(f"Employee with id:{emp_id} was deleted")

        elif action == 3:
            employees = dao.get_all()
            if not employees:
                print("No employees in database")
            else:
                for emp in employees:
                    print(emp)

        elif action == 4:
            emp_id = int(input("Enter employee id to get: "))
            emp = dao.get_by_id(emp_id)
            if emp:
                print(f"Employee Details:\n{emp}")
            else:
                print("No such employee found")

        elif action == 5:
            try:
                emp_id = int(input("Enter employee id to update: "))
                emp_info = input("Enter new employee info (name, position, salary, hire date YYYY-MM-DD): ")
                name, position, salary, hire_date = emp_info.split(", ")
                updated_emp = Employee(emp_id, name, position, float(salary), hire_date)
                dao.update(emp_id, updated_emp)
                print("Employee info was modified")
            except Exception as e:
                print(f"Oops, Error: {e}")

        elif action == 6:
            check = input("Are you sure you want to delete ALL employees? (yes/no): ").lower()
            if check == "yes":
                dao.delete_all()
                print("All employees were deleted")

        elif action == 7:
            break

        else:
            print("Sorry, no such action")

    dao.close()