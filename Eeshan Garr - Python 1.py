# Python Workshop 1: Variables
""" KEY
+ Concept -> Make sure to read these out loud
@ Code Explanation -> Paraphrase these as necessary
& Interaction with Students -> These are suggestions, interact with students based on your best judgement
! Run the Code -> Press the run button and examine the output with students
"""

print("Hello World")
#!
#+ print() tells the program to print out whatever is in the quotes inside the parentheses
#+ Make sure students understand they need surrounding quotes when printing out words

print(3, end="")
print(5)
print(6)
#!
#+ Code is run from top to bottom line by line
#+ end="" will create a new line after the printed output
#@ 3 is printed and a new line is added. Then 5 and 6 are printed on the same line, resulting in 56

print(5+6)
print(7*8)
print(9-200)
print(100/5)
#!
#+ Python has operators that can do basic math; + means addition, - means subtraction, * means multiplication, / means division

print(23%5)
#!
#+ The modulo operator % returns the remainder from performing division
#@ 23 divided by 5 is 4 with a remainder of 3, which is why 3 is printed

print(3+7*2)
#!
#+ Math operations in Python follow PEMDAS. However, parentheses do not indicate multiplication. 
#+ Modulo % and Multiplication * are both M in PEMDAS
#& Have students create and solve a math problem of their own

y = 5
#@ This declares an integer variable called y and sets its value to 5 
#+ Variables store information (numbers, words, etc.) and can be modified

print(y)
#!
#@ This prints out the value stored in variable y which is 5

a = 10
b = 10.0
print(a/7) 
print(b/7)
#!
#+ When an integer is divided by an integer, the stuff after the result's decimal point is removed/truncated
#@ This is why a/7 gives 1, because 10/7 is 1 with a remainder of 3.
#+ When a decimal is divided by anything, the answer keeps its decimal point
#@ This is why b/7 gives 1.428..., because b started as a decimal


c = 'c'
d = "Code Future"
print(c)
print(d)
#!
#+ Variables have multiple differnt types, these two are called strings and chars
#+ Strings are words and sentences while chars are single characters
#+ Strings are indicated by double quotes ""
#+ chars are indicated by single quotes ''

x = 1
x = x + 1
print(x)
#!
#@ This assigns x to a new value of (x+1) and prints it out

x += 1
#+ In-Place Operators shorten the way you write x = x + (a number) to x += (a number)

x -= 1 
print(x)
#@ In-Place Operators and -- instead of ++ work for subtraction like they work for addition

print("Code Future")
# This is a comment 
#print("Code Future");
#+ Single line comments can be made with a // preceding the comment
#+ Commented lines are not run by the program
#+ Comments can be helpful notes for the developer 
        
""" 
Line 1 
Line 2
Line 3
"""
#+ Multiline comments can be made with a ''' preceding the comment and a ''' ending it
#& Have students comment out all their current code with a multiline comment and have them try running it to show that their code won't run when it is commented out

x = "one"

print("I have " + x + " computer")
#!
#+ Concatenation: By using the + signs, Strings can be added together with other strings

x = 1
print("I have " + x + " computer")
#! 
#@ This does not work because Python cannot concatenate between different types 

print("I have " + str(x) + " computer")
#! 
#@ This works and prints out "I have 1 computer"
#+ str() typecasts, which means changes the type, of its input (in this case x) from an integer into a string
        
print("\"This is cool\"- Code ", end = "")
print(" Future")
print("I\nLOVE\nCODING")
#!
#+ Escape Characters - Special characters like "" used in Python can be used in print statements when preceded by \ which is called a backslash 
#+ Newlines can be created in a String using \n
#+ Python adds a new line to the end of each print statement automatically. To bypass this, we put a comma and then end = "", putting in the quotes whatever we want python to add to the end of the print statment. 
#@ The end = "" will make it so nothing is added to the end of the print statement 
#& With the remaining time, challenge students to print out word problems and then print out their solutions to each other's problems
#& Make sure they use concatenation to print out solutions using both words and numbers, also have them use Java to do the calculations

