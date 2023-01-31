import mysql.connector

connect = mysql.connector.connect(host="35.238.148.78", port = "3306", user="staniswinata", password = "staniswinata07", database = "event", auth_plugin = "mysql_native_password")
cursor = connect.cursor()


def getEvents():
    cursor.execute("Select * from Event")
    return cursor.fetchall()
def getCommittees():
    cursor.execute("Select * from Committees")
    return cursor.fetchall()
def getPositions():
    cursor.execute("Select * from JobPosition")
    return cursor.fetchall()
def getPurchase():
    cursor.execute("Select * from Purchase")
    return cursor.fetchall()
def getTickets():
    cursor.execute("Select * from Tickets")
    return cursor.fetchall()
def getTicketStatus():
    cursor.execute("Select * from TicketStatus")
    return cursor.fetchall()
def getSalary():
    cursor.execute("Select * from Salary")
    return cursor.fetchall()
def getUserInfo():
    cursor.execute("Select UserID, firstName, lastName, Username from UserInfo")
    return cursor.fetchall()

def getPositionlist():
    sql = "Select PositionName from JobPosition"
    cursor.execute(sql)
    x = [i[0] for i in cursor.fetchall()]
    return x

def getPositionName(id):
    sql = "SELECT PositionName FROM JobPosition WHERE PositionID = %s"
    value = (id,)
    cursor.execute(sql, value)
    y = cursor.fetchall()
    name = [i[0] for i in y]
    return name[0]

def getPositionID(name):
    sql = "SELECT PositionID FROM JobPosition WHERE PositionName = %s"
    value = (name,)
    cursor.execute(sql, value)
    y = cursor.fetchall()
    pid = [i[0] for i in y]
    return pid[0]
