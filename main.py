#!/usr/bin/python

import subprocess

ans=True
newMenu=False
question="What would you like to do? \n"

#Function that calls logger.py script which logs the activity in a txt file
def loggerFn(script,arguments = ""):
  if script != "":
    script = ' -s ' + script
  if arguments != "":
    arguments = ' -a ' + f'"{arguments}"'
  subprocess.call(' python logger.py' + script + arguments, shell=True)

print ("\n Welcome to my program!")
print ("Select the number from the list")
while ans:
    print("""
    1.Command with input
    2.Open me!
    3.Shell Command
    4.Exit/Quit
    """)
    ans=input(question)
    if ans=="1":
      print("\n--Script where you input your name--")
      ans1=input("Enter your first name ")
      ans2=input("Enter your last name ")  
      if ans1=="":
        print("No first Name entered.")
      else:
        ans1=" -f " + ans1
      if ans2=="":
        print("No last name entered.") 
      else:
        ans2=" -l " + ans2   
      #subprocess.call(["python", "inputYourName.py"]) #different method of capturing users name/ID
      subprocess.call(" python inputYourName.py" + ans1 + ans2, shell=True)
      loggerFn("inputYourName.py", ans1 + ans2)
    elif ans=="2":
      newMenu=True
      print("\n New Menu")
      while newMenu:
          print("""
          1.Let me know your favourite color
          2.Go Back to main menu
          3.Exit
          """)
          newMenu=input(question)
          if newMenu=="1":
              print("\n--Script where you share your fav color!--")
              color=" " + input("What is your favourite color? ")
              subprocess.call(" python favColor.py" + color, shell=True)
              loggerFn("favColor.py",color)
          elif newMenu=="2":
              print("\n Back to main menu")
              newMenu = None
          elif newMenu=="3":
              print("\n Exit")
              newMenu = None
              ans = None
          else:
            print("\n Not Valid Choice Try again")
    elif ans=="3":
      subprocess.call(['sh', 'shellScript.sh'])
      loggerFn('shellScript.sh')
    elif ans=="4":
      print("\n Exit")
      ans = None
    else:
       print("\n Not Valid Choice Try again")