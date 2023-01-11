import gui.Selection.mainSelection
import gui.View.main
import gui.View.userview
import gui.Login.Login
import gui.Signup.Signup

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