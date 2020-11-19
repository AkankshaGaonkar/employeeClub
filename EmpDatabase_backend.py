import sqlite3
#Backend

def employeeData():
    con=sqlite3.connect("employee.db")
    cur =con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, EmpID text, Firstname text, Surname text, DOB text, Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()

def addEmpRec(EmpID, Firstname, Surname, DOB , Age , Gender , Address , Mobile):
    con=sqlite3.connect("employee.db")
    cur =con.cursor()
    cur.execute("INSERT INTO employee VALUES (NULL, ?,?,?,?,?,?,?,?)",EmpID , Firstname , Surname , DOB , Age , Gender , Address , Mobile)
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("employee.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM employee")
    rows =cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con=sqlite3.connect("employee.db")
    cur =con.cursor()
    cur.execute("DELETE FROM employee WHERE id=?",(id))
    con.commit()
    con.close()

def searchData(EmpID="", Firstname="" , Surname="" , DOB="" , Age="" , Gender="" , Address="" , Mobile=""):
    con=sqlite3.connect("employee.db")
    cur =con.cursor()
    cur.execute("SELECT  * FROM student WHERE EmpID=? OR Firstname=? OR Surname=? , DOB=? , Age=? , Gender=? , Address=? , Mobile=?",(EmpID, Firstname, Surname, DOB, Age, Gender, Address, Mobile))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,EmpID="", Firstname="" , Surname="" , DOB="" , Age="" , Gender="" , Address="" , Mobile=""):
    con=sqlite3.connect("employee.db")
    cur =con.cursor()
    cur.execute("UPDATE student SET EmpID=? OR Firstname=? OR Surname=? , DOB=? , Age=? , Gender=? , Address=? , Mobile=?",(EmpID, Firstname, Surname, DOB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()


employeeData()
