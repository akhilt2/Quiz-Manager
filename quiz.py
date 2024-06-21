#!/usr/bin/python3
score=0 #To keep track of score
#Using a function so we don't need to write code many times:)
def quiz(qn,op1,op2,op3,op4,cr): #Accepts question as first parameter, 4 options as 2nd to 5th parameter and correct option as 6th parameter
    print(qn)
    print("1) "+op1,"2) "+op2,"3) "+op3,"4) "+op4,sep='\t') #I used \t because it adds space in between the options. Also added option numbers so the user can input the correct number
    n=input("Enter the option or option number: ").lower() #Take user input and make it lowercase
    if cr==n or locals()['op'+cr].lower()==n: #Checks whether user input is correct. Used locals() so we can get the correct answer and check with user input. Also it can check whether the option number entered by user is correct.
        print("Correct Answer :)")
        global score #use global score variable
        score+=1 #update the score
    else:
        print("Wrong Answer :(")
#Asking questions using the quiz function
quiz("Which is the tiling window manager from the following?","KDE","GNOME","Hyprland","Cinnamon","3")
quiz("What does a cat say?","Vroom Vroom","Mauw","Haha","Whatsup my bro","2")
quiz("Which is the mascot of Linux kernal?","GNU","Pego","SpongeBob","Tux","4")
print("Your score is",str(score)+"/3")
