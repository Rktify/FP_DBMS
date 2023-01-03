import mysql.connector
import os

connect = mysql.connector.connect(host="35.238.148.78", port = "3306", user="staniswinata", password = "staniswinata07", database = "event", auth_plugin = "mysql_native_password")
cursor = connect.cursor()

def getEvents():
    cursor.execute("Select * from Event")
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()