import gui.Selection.mainSelection
import gui.View.main
import gui.View.userview
import gui.Login.Login
import gui.Signup.Signup
import gui.Selection.userSelection
import gui.Purchase.Purchase
import gui.Hub.mainHub
import gui.Manage.Redirect

def goView():
    gui.View.main.viewWindow()

def goSelection():
    gui.Selection.mainSelection.selectionWindow()

def gouserView():
    gui.View.userview.userviewWindow()

def goLogin():
    gui.Login.Login.loginWindow()

def goSignup():
    gui.Signup.Signup.signupWindow()

def gouserSelection():
    gui.Selection.userSelection.selectionWindow()

def goPurchase():
    gui.Purchase.Purchase.purchaseWindow()

def goHub():
    gui.Hub.mainHub.hubWindow()

def goEvent():
    print("Events Table")
    gui.Manage.Redirect.goEvent()
def goCommittees():
    print("Committees Table")
    gui.Manage.Redirect.goCommittees()
def goPurchased():
    print("Purchase Table")
    gui.Manage.Redirect.goPurchase()
def goPosition():
    print("Position Table")
    gui.Manage.Redirect.goPosition()
def goTickets():
    print("Tickets Table")
    gui.Manage.Redirect.goTickets()
def goTicketStatus():
    print("Tickets Status Table")
    gui.Manage.Redirect.goTicketStatus()
def goUserInfo():
    print("User Info Table")
    gui.Manage.Redirect.goUserInfo()