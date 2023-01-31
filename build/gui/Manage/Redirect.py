import gui.Manage.Committees.main
import gui.Manage.Event.main
import gui.Manage.Purchase.main
import gui.Manage.Position.main
import gui.Manage.Tickets.main
import gui.Manage.TicketStatus.main
import gui.Manage.UserInfo.main
import gui.Manage.Salary.main
from .. import Redirect

def goEvent():
    print("Event Table")
    gui.Manage.Event.main.eventWindow()
def goCommittees():
    print("Committees Table")
    gui.Manage.Committees.main.committeesWindow()
def goPurchase():
    print("Purchase Table")
    gui.Manage.Purchase.main.purchaseWindow()
def goPosition():
    print("Position Table")
    gui.Manage.Position.main.positionWindow()
def goTickets():
    print("Tickets Table")
    gui.Manage.Tickets.main.ticketsWindow()
def goTicketStatus():
    print("Tickets Status Table")
    gui.Manage.TicketStatus.main.ticketstatusWindow()
def goUserInfo():
    print("User Info Table")
    gui.Manage.UserInfo.main.userWindow()
def goSalary():
    print("Salary Table")
    gui.Manage.Salary.main.salaryWindow()
def goSelection():
    print("Back to Selection")
    Redirect.goSelection()
def goHub():
    print("Back to Hub")
    Redirect.goHub()