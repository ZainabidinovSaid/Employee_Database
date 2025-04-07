from employee_class import Employee
import sqlite3


class EmployeeDAO:
    def __init__(self, db_name="employee_db.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                salary REAL NOT NULL,
                hire_date TEXT NOT NULL
            )
        """)
        self.conn.commit()
    def insert(self, employee: Employee):
        if self.get_by_id(employee.id):
            print(f"Employee with id:{employee.id} already exists in database")
        else:
            self.cursor.execute("""
                INSERT INTO employee (id, name, position, salary, hire_date)
                VALUES (?, ?, ?, ?, ?)""", (employee.id, employee.name, employee.position, employee.salary, employee.hireDate))
            self.conn.commit()
            print('Employee added')

    def get_by_id(self, emp_id):
        self.cursor.execute("SELECT * FROM employee WHERE id = ?", (emp_id,))
        emp_row = self.cursor.fetchone()
        if emp_row:
            return Employee(*emp_row)
        return None

    def get_all(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()
        return [Employee(*x) for x in rows]

    def update(self, id, employee: Employee):
        self.cursor.execute("""
            UPDATE employee SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?""", (employee.name, employee.position, employee.salary, employee.hireDate, id))
        self.conn.commit()

    def delete(self, emp_id):
        self.cursor.execute("DELETE FROM employee WHERE id = ?", emp_id)
        self.conn.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM employee")
        self.conn.commit()

    def close(self):
        self.conn.close()