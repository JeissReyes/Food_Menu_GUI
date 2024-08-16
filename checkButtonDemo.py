""" 
Program: checkButtonDemo.py
Chapter 8 (Page 281)
8/13/2024
**Note: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based app demonstrating the use of the checkbutton (checkbox) graphic component
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports can go here

# Class header (class name will change project to project)
class CheckButton(EasyFrame):
    
    # Defintion of our class' constructor method
    def __init__(self):
        # Call to the Easy Frame class constructor
        EasyFrame.__init__(self, title = "Menu Options", width = 320, height = 200, resizable = False, background = "#F08700")

        # Add various components to the window
        self.addLabel(text = "Today's Menu", row = 0, column = 0, columnspan = 2, sticky = "NWSE", background = "#EFCA08", foreground = "#00A6A6", font = Font(family = "Elephant", size = 28, slant = "italic"))

        # Add four check buttons and adjust colors
        self.chickCB = self.addCheckbutton(text = "Chicken", row = 1, column = 0)
        self.chickCB["background"] = "#EFCA08"
        self.chickCB["foreground"] = "#00A6A6"

        self.taterCB = self.addCheckbutton(text = "French Fries", row = 1, column = 1)
        self.taterCB["background"] = "#EFCA08"
        self.taterCB["foreground"] = "#00A6A6"

        self.beanCB = self.addCheckbutton(text = "Green Beans", row = 2, column = 0)
        self.beanCB["background"] = "#EFCA08"
        self.beanCB["foreground"] = "#00A6A6"

        self.sauceCB = self.addCheckbutton(text = "Applesauce", row = 2, column = 1)
        self.sauceCB["background"] = "#EFCA08"
        self.sauceCB["foreground"] = "#00A6A6"

        # Add the command button and adjust attributes
        self.order = self.addButton(text = "Place Order", row = 3, column = 0, columnspan = 2, command = self.placeOrder )
        self.order["background"] = "#BBDEF0"
        self.order["foreground"] = "#00A6A6"
        self.order["width"] = 24
        self.order["height"] = 2

    # Definition of the placeOrder() function
    def placeOrder(self):
        # Display a message box with the order summary
        message = ""

        # Analyze each checkbutton to see if it has been checked marked
        if self.chickCB.isChecked():
            message += "Chicken\n\n"

        if self.taterCB.isChecked():
            message += "French Fries\n\n"

        if self.beanCB.isChecked():
            message += "Green Beans\n\n"

        if self.sauceCB.isChecked():
            message += "Applesauce\n"

        if message == "":
            message = "Sorry, no food was ordered!"

        # Now that we have looked at every checkbutton, let's push the message variable to a pop-up window
        self.messageBox(title = "Customer Order", message = message)

    
# Global definition of the main() method
def main():
    # Instantiate an object from the class into mainloop()
    CheckButton().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
    main()
