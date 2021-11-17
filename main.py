#Jonas Kennedy, 11/17/21, program which determinds if a triangle is equillateral, isoceles or, scalene

#Defining call functions for drawing the traingle 
def triangle1():
  print("Equillateral traingle drawing")
def triangle2():
  print("isoceles triangle drawing")
def triangle3 ():
  print("scalene triangle drawing")
side1 = int(input("What is the length of the 1st side? \n"))
side2 = int(input("what is the length of the 2nd side? \n"))
side3 = int(input("what is the length of the 3rd side? \n"))
if side1==side2 and side1==side3 and side2==side3:
  print("Equillateral triangle \n")
  #Function calling example below
  triangle1()
elif side1==side2 or side2==side3 or side1==side3:
  print("isoceles traingle \n")
  triangle2()
else:
  print("scalene traingle \n")
  triangle3()
