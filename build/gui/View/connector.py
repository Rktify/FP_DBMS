import mysql.connector
import os

connect = mysql.connector.connect(host="35.238.148.78", port = "3306", user="staniswinata", password = "staniswinata07", database = "event", auth_plugin = "mysql_native_password")
cursor = connect.cursor()

def getEvents():
    cursor.execute("Select * from Event")
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()
def getCommittees():
    cursor.execute("Select * from Committees")
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()
def getPositions():
    cursor.execute("Select * from JobPosition")
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()
def getParticipants():
    cursor.execute("Select * from Participants")
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()
def getTickets():
    cursor.execute("Select * from Tickets")
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()
def getTicketStats():
    cursor.execute("Select * from TicketStatus")
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()
