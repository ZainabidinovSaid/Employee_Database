
# Employee Management System

## Overview

The **Employee Management System** is a Python-based application that interacts with an **SQLite database** to perform CRUD (Create, Read, Update, Delete) operations on employee records. The system allows users to manage employee information such as ID, name, position, salary, and hire date.

This system provides an interactive **Command-Line Interface (CLI)** for users to manage employee records and perform various operations.

## Features

- **SQLite Database**: Stores employee details in a structured format.
- **Employee Class**: Represents an employee with attributes like `id`, `name`, `position`, `salary`, and `hire_date`.
- **EmployeeDAO Class**: Handles database operations like inserting, retrieving, updating, and deleting employee records.
- **CLI Menu**: Provides an interactive menu to the user for managing employee data.

## Table Structure

The **employee** table in the database contains the following columns:

| Column     | Type    | Constraints                    |
|------------|---------|--------------------------------|
| `id`       | INTEGER | PRIMARY KEY, AUTO-INCREMENT    |
| `name`     | TEXT    | NOT NULL                       |
| `position` | TEXT    | NOT NULL                       |
| `salary`   | REAL    | NOT NULL                       |
| `hire_date`| TEXT    | NOT NULL (YYYY-MM-DD format)   |

## Usage

Once the program is running, you will be presented with a menu of actions that you can perform. Below are the available options:

### 1. Add Employee
- Input: You will be prompted to enter the employee's details.
- Example Input:
  ```
  Choose the action: 1
  Enter employee's info (id, name, position, salary, hire date YYYY-MM-DD): 1, Saidislom Zainabidinov, Data Analyst, 70000, 2024-06-17
  ```
- Output:
  ```
  Employee added
  ```

### 2. Delete Employee by ID
- Input: You will be prompted to enter the ID of the employee to delete.
- Example Input:
  ```
  Choose the action: 2
  Enter employee id to delete: 6
  ```
- Output:
  ```
  Employee with id:6 was deleted
  ```

### 3. View All Employees
- Input: View all employees stored in the database.
- Example Input:
  ```
  Choose the action: 3
  ```
- Output:
  ```
  ID: 1, Name: Saidislom Zainabidinov, Position: Data Analyst, Salary: 70000.0, Hire date: 2024-06-17
  ID: 2, Name: John Doe, Position: Software Engineer, Salary: 65000.0, Hire date: 2020-01-01
  ...
  ```

### 4. Get Employee by ID
- Input: You will be prompted to enter the employee ID.
- Example Input:
  ```
  Choose the action: 4
  Enter employee id to get: 1
  ```
- Output:
  ```
  Employee Details:
  ID: 1, Name: Saidislom Zainabidinov, Position: Data Analyst, Salary: 70000.0, Hire date: 2024-06-17
  ```

### 5. Update Employee Information
- Input: You will be prompted to enter the employee ID and new employee details.
- Example Input:
  ```
  Choose the action: 5
  Enter employee id to update: 1
  Enter new employee info (name, position, salary, hire date YYYY-MM-DD): Saidislom Zainabidinov, AI/ML engineer, 75000, 2024-11-27
  ```
- Output:
  ```
  Employee info was modified
  ```

### 6. Delete All Employees
- Input: You will be prompted for confirmation to delete all employees.
- Example Input:
  ```
  Choose the action: 6
  Are you sure you want to delete ALL employees? (yes/no): yes
  ```
- Output:
  ```
  All employees were deleted
  ```

### 7. Exit
- Input: Exit the program.
- Example Input:
  ```
  Choose the action: 7
  ```
- Output:
  ```
  Process finished with exit code 0
  ```

## Example Run

```
Employee database
1. Add employee
2. Delete employee by id
3. See all employees
4. Get employee by id
5. Update employee information by id
6. Delete all employees
7. Exit
Choose the action: 1
Enter employee's info (id, name, position, salary, hire date YYYY-MM-DD): 1, Saidislom Zainabidinov, Data Analyst, 70000.0, 2024-06-17
Employee added

Choose the action: 3
ID: 1, Name: Saidislom Zainabidinov, Position: Data Analyst, Salary: 70000, Hire date: 2024-06-17
ID: 2, Name: John Doe, Position: Software Engineer, Salary: 65000.0, Hire date: 2020-01-01
...
```
