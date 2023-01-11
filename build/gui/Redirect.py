import gui.Selection.mainSelection
import gui.View.main
import gui.View.userview
import gui.Login.Login
import gui.Signup.Signup
import gui.Selection.userSelection
import gui.Purchase.Purchase

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