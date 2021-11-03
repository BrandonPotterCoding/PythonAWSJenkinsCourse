validInput = ["R","P","S"]
userChoice= "k"
secondChoice = "l"
while userChoice not in validInput:
    userChoice = input("Enter in (R)ock, (P)aper, or (S)cissors for first user: ")
    userChoice.upper()

while secondChoice not in validInput:
    secondChoice = input("Enter in (R)ock, (P)aper, or (S)cissors for second user: ")
    secondChoice.upper()

if userChoice == "R" :
    if secondChoice == "S": print("First user wins")
    elif secondChoice.casefold() == "P": print("Second user wins")
    elif secondChoice == "R": print("Its a Tie")
    
if userChoice == "P" :
    if secondChoice == "R": print("First user wins")
    elif secondChoice == "S": print("Second user wins")
    elif secondChoice == "P": print("Its a Tie")
    
if userChoice == "S" :
    if secondChoice == "P": print("First user wins")
    elif secondChoice == "R": print("Second user wins")
    elif secondChoice == "S": print("Its a Tie")