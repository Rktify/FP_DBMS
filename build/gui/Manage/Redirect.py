import gui.Manage.Committees.main
import gui.Manage.Event.main
import gui.Manage.Participants.main
import gui.Manage.Position.main
import gui.Manage.Tickets.main
# import Manage.TicketStats.main
from .. import Redirect

def goEvent():
    print("Event Table")
    gui.Manage.Event.main.eventWindow()
def goCommittees():
    print("Committees Table")
    gui.Manage.Committees.main.committeesWindow()
def goParticipants():
    print("Participants Table")
    gui.Manage.Participants.main.participantsWindow()
def goPosition():
    print("Position Table")
    gui.Manage.Position.main.positionWindow()
def goTickets():
    print("Tickets Table")
    gui.Manage.Tickets.main.ticketsWindow()
def goSelection():
    print("Back to Selection")
    Redirect.goSelection()