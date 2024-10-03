from Python.model.Employee import Employee
from Python.repo.BaseRepository import connect
from mysql.connector import Error
def formatDate(data):
        return data.strftime("%d/%m/%Y")
def transFormData(data):
    return Employee(data[0], data[1], formatDate(data[2]), data[3], convert_gender(data[4]), data[5], data[6])
def convert_gender(self):
        if(self._gender==1):
            self._gender="Male"
        else:
            self._gender="Female"
def findAll():
    query = 'SELECT * FROM employee'
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    my_list = []
    for row in results:
        my_list.append(row)
    return my_list

    

def insert(emp):
    query='INSERT INTO employee (`gender`, `birth_day`, `address`, `full_name`, `id_card`,`phone`) VALUES (%s,%s,%s,%s,%s,%s) '
    parameter = (emp.gender, emp.birthday, emp.address, emp.fullName, emp.idCard, emp.phone)
    print(parameter)
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query, parameter)
        connection.commit()
        print("Insert success")
    except Error as e:
     print(f"Error inserting employee: {e}")
def update(emp):
    query='UPDATE employee SET gender = %s, birth_day = %s, address = %s, full_name = %s, id_card = %s, phone = %s WHERE employee_id = %s '
    parameter = (emp.gender, emp.birthday, emp.address, emp.fullName, emp.idCard, emp.phone, emp.id)
    print(parameter)
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query, parameter)
        connection.commit()
        print("Update success")
    except Error as e:
     print(f"Error inserting employee: {e}")
def findById(emp_id):
    query = 'SELECT * FROM employee WHERE employee_id = %s'
    parameter = (emp_id,)
    connection = None
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query, parameter)
        result = cursor.fetchone()
        return result
    except Error as e:
        print(f"Error finding employee: {e}")
        return None
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
def delete(emp_id):
    query='delete FROM employee WHERE employee_id = %s '
    parameter = (emp_id,)
    try:
        connection = connect()
        cursor = connection.cursor()
        employee = findById(emp_id)
        if employee is not None:
           cursor.execute(query, parameter)
           connection.commit()
           print("Delete success")
        else:
            print("Employee not found")
    except Error as e:
     print(f"Error delete employee: {e}")











