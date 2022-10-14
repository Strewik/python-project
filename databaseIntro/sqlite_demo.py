import sqlite3
from employee import Employee

conn  = sqlite3.connect('employee.db')

db = conn.cursor()

# db.execute('''CREATE TABLE employee (
#     first text,
#     last text,
#     pay integer
#     )''')

def insert_emp(emp):
    with conn:
        db.execute("INSERT INTO employee VALUES (:first, :last, :pay)", 
                   {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

emp_1 = Employee('John', 'Doe', 6000)
emp_2 = Employee('Jane', 'Doe', 7000)

insert_emp(emp_1)
insert_emp(emp_2)

conn.commit()
# db.execute("INSERT INTO employee VALUES ('jane', 'jordan', 5000)")
# db.execute("INSERT INTO employee VALUES ('mike', 'jordan', 5000)")
# db.execute("INSERT INTO employee VALUES ('quick', 'jordan', 5000)")

db.execute("SELECT * FROM employee WHERE last = 'jordan'")
db.execute("SELECT * FROM employee WHERE last = 'Doe'")

print(db.fetchall())

def get_emps_by_name(lastname):
    db.execute("SELECT * FROM employee WHERE last=:last", {'last': lastname})
    return db.fetchall()

def update_pay(emp, pay):
    with conn:
        db.execute("""UPDATE employee SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})
        
def remove_emp(emp):
    with conn:
        db.execute("DELETE FROM employee WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})
        
# remove_emp("Jane", "Doe")

conn.close()

