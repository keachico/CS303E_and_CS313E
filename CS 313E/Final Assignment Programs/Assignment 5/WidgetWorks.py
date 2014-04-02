#  Files: WidgetWorks.py
#
#  Description: Use a Queue class to implement an automated ordering system
#
#  Student's Name: Nadeem Abha, Kevin Achico
#
#  Student's UT EID: na4333, ka6893
#
#  Course Name: CS 313E 
#
#  Date Created: 10/11/12
#
#  Date Last Modified: 10/15/12

# Import the Queue class
from MyQueue import *


# Create the Order class
class Order:

    orderNum = 1
    # The class takes three arguments
    def __init__(self, name, color, quantity):
        self._orderNum = Order.orderNum
        self._customerName = name
        self._customerColor = color
        self._customerQuantity = quantity
        Order.orderNum += 1

    # These are the getters or accessors for the three
    # arguments and order number
    def getOrderNum(self):
        return self._orderNum

    def getCustomerName(self):
        return self._customerName

    def getCustomerColor(self):
        return self._customerColor

    def getCustomerQuantity(self):
        return self._customerQuantity

    # These are the setters or mutators for the three
    # arguments and order number
    def setOrderNum(self, num):
        self._orderNum = num

    def setCustomerName(self, name):
        self._customerName = name

    def setCustomerColor(self, color):
        self._customerColor = color

    def setCustomerQuantity(self, quantity):
        self._customerQuantity = quantity

    def __str__(self):
        print (self._customerName, self._customerColor, self._customerQuantity)
        

# Top level function that runs the program        
def TestFactory():

    # Create a list of colors to compare with user input, if the color is not in
    # the list, cancel the order
    color_choice = ["red", "white", "blue"]
    customer_orders = MyQueue()
    # Intitalize a boolean
    b = True
    while b :

        print("Welcome to the Waskelly Wabbit Wiget Works automated odering system!")
        print("")
        name = input("\t Please input customer name (or exit): ")
        # If the User enters exit, break out of the loop
        if name == "exit":
            break
        color = input("\t Please select desired widget color (red, white, blue): ")
        # If the color isnt one of the choices given, continue 
        if color_choice.count(color) == 0:
            print("Sorry, that's not a color we offer. Order cancelled. \n")
            continue
        
        quantity = input("\t Excellent choice. How many %s widgets do you want? "%(color))
        # If the number given is not a valid positive integer, continue
        if not quantity.isdigit():
            print("Bad quantity. Order cancelled \n")
            continue
        
        print("Order confirmed! Please shop with us again. \n")
        customer_orders.enqueue(Order(name, color, quantity))

    print("")
    print ("Now processing orders:")

    # While the Queue is full
    while not customer_orders.isEmpty():
        
        # Use the getter or accessors from the Order class
        processed_Order = customer_orders.dequeue()
        order_Num = processed_Order.getOrderNum()
        order_Name = processed_Order.getCustomerName()
        order_Color = processed_Order.getCustomerColor()
        order_Quantity = processed_Order.getCustomerQuantity()
        
        # Print the orders and their values out
        print ("     Order Shipped: \t Order %d: customer %s requests %s %s widgets." \
              % (order_Num, order_Name, order_Quantity,order_Color))
    # Since the while loop broke, the Queue is empty
    print("Queue empty.")
            

    
    

TestFactory()
