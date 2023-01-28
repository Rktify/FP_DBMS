import mysql.connector

connect = mysql.connector.connect(host="35.238.148.78", port = "3306", user="staniswinata", password = "staniswinata07", database = "event", auth_plugin = "mysql_native_password")
cursor = connect.cursor()

def getEvents():
    cursor.execute("Select * from Event")
    return cursor.fetchall()
def getCommittees():
    cursor.execute("SELECT c.CommitteesID, c.Name, p.PositionName, e.EventName FROM Committees c JOIN JobPosition p ON c.PositionID = p.PositionID JOIN Event e ON c.EventID = e.EventID")
    return cursor.fetchall()
def getPositions():
    cursor.execute("Select p.PositionID, p.PositionName, p.Salary, e.EventName FROM JobPosition p JOIN Event e ON p.EventID = e.EventID")
    return cursor.fetchall()
def getParticipants():
    cursor.execute("Select * from Participants")
    return cursor.fetchall()
def getTickets():
    cursor.execute("Select t.TicketID, e.EventName, t.TicketType, s.TicketStatus FROM Tickets t JOIN Event e ON t.EventID = e.EventID JOIN TicketStatus s ON t.TicketStatusID = s.TicketStatusID")
    return cursor.fetchall()
def getTicketStats():
    cursor.execute("Select * from TicketStatus")
    return cursor.fetchall()
def getUserInfo():
    cursor.execute("Select UserID, firstName, lastName, Username from UserInfo")
    return cursor.fetchall()

def getTicketss():
    cursor.execute("SELECT t.TicketID, e.EventName, t.TicketType, s.TicketStatus FROM Tickets t JOIN Event e ON t.EventID = e.EventID JOIN TicketStatus s ON t.TicketStatusID = s.TicketStatusID;")
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


def checkCredentials(user, passw):
    cursor.execute(f"Select userName from UserInfo")
    x = [i[0] for i in cursor.fetchall()]
    for i in range(len(x)):
        if user == x[i]:
            cursor.execute(f'Select password from UserInfo where userName = "{user}"')
            x = [i[0] for i in cursor.fetchall()]
            if passw == x[0]:
                return True
            else:
                return False

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

def checkuserAvailability(user):
    cursor.execute(f"Select userName from UserInfo")
    y = cursor.fetchall()
    x = [i[0] for i in y]
    for i in range(len(x)):
        if user == x[i]:
            return False
    return True

def getID(user):
    cursor.execute(f"SELECT UserID FROM UserInfo WHERE userName = '{user}'")
    x = [i[0] for i in cursor.fetchall()]
    return x[0]
