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
def getParticipants():
    cursor.execute("Select * from Participants")
    return cursor.fetchall()
def getTickets():
    cursor.execute("Select * from Tickets")
    return cursor.fetchall()
def getTicketStats():
    cursor.execute("Select * from TicketStatus")
    return cursor.fetchall()
def getUserInfo():
    cursor.execute("Select UserID, firstName, lastName from UserInfo")
    return cursor.fetchall()
    
def getTicketss():
    cursor.execute("SELECT t.TicketID, e.EventName, t.TicketType, s.TicketStatus from Tickets t join Event e ON t.EventID = e.EventID join TicketStatus s ON t.TicketStatusID = s.TicketStatusID;")
    return cursor.fetchall()

def getPurchased():
    cursor.execute("SELECT t.TicketID, t.TicketType, e.EventID, e.EventName, e.Location, e.Date, e.Time FROM Tickets t JOIN Event e ON e.EventID = t.EventID WHERE t.TicketStatusID = 2")
    return cursor.fetchall()

def getPurchase():
    cursor.execute("SELECT t.TicketID, t.TicketType, e.EventID, e.EventName, e.Location, e.Date, e.Time FROM Tickets t JOIN Event e ON e.EventID = t.EventID WHERE t.TicketStatusID = 1")
    return cursor.fetchall()

def getnextuserID():
    cursor.execute("Select UserID from UserInfo")
    x = [i[0] for i in cursor.fetchall()]
    return (x[-1] + 1)

def getnextID():
    cursor.execute("Select TicketID from UserInfo")
    x = [i[0] for i in cursor.fetchall()]
    return (x[-1] + 1)

def getnextpurchaseID():
    cursor.execute("Select PurchaseID from Purchase")
    x = [i[0] for i in cursor.fetchall()]
    return (x[-1] + 1)

def checkuserName(id, user):
    cursor.execute(f"Select userName from UserInfo WHERE UserID = {id}")
    x = [i[0] for i in cursor.fetchall()]
    if user == x[0]:
        return True
    else:
        return False

def checkPassword(id, passw):
    cursor.execute(f"Select password from UserInfo WHERE UserID = {id}")
    x = [i[0] for i in cursor.fetchall()]
    if passw == x[0]:
        return True
    else:
        return False

def forgotPassword(user):
    cursor.execute(f"Select Password, UserID from UserInfo WHERE userName = '{user}'")
    y = cursor.fetchall()
    x = [i[0] for i in y]
    z = [i[1] for i in y]
    return x[0], z[0]

def checkAvailablity(id):
    cursor.execute(f"Select TicketID from Purchase")
    y = cursor.fetchall()
    x = [i[0] for i in y]
    for i in range(len(x)):
        if id == x[i]:
            return False
        else:
            cursor.execute(f"UPDATE Tickets SET TicketStatusID = 2 WHERE TicketID = {id}")
            connect.commit()
            return True



