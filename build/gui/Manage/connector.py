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
def getUserInfo():
    cursor.execute("Select UserID, firstName, lastName from UserInfo")
    return cursor.fetchall()
