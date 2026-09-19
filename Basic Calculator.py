Error = True
programchoice = None
while Error:
    programchoice = input("Please, select your program! (Only 2 numbers!)\n1 | Addition \n2 | Subtraction \n3 | Multiplication \n4 | Division \n")
    programchoice = int(programchoice)
    if programchoice == 1 or programchoice == 2 or programchoice == 3 or programchoice == 4:
        Error = False 
    else:
        print("Error! You can only select programs from 1 to 4")                    

FirstNumber = float (input("Please, enter a number!\t"))
SecondNumber = float (input("Please, enter a number!\t"))

def Addition (FirstNumber, SecondNumber):
    return FirstNumber + SecondNumber

def Subtraction (FirstNumber, SecondNumber):
    return FirstNumber - SecondNumber

def Multiplication (FirstNumber, SecondNumber):
    return FirstNumber * SecondNumber

def Division (FirstNumber, SecondNumber):
    return FirstNumber / SecondNumber

if programchoice == 4:
    while SecondNumber == 0:
       SecondNumber = float (input("Error! Cant proceed while the Second Number is 0! Please, enter a correct number!\t")) 

if programchoice == 1:
    print(f"Result: {Addition(FirstNumber, SecondNumber)}")
elif programchoice == 2:
    print(f"Result: {Subtraction(FirstNumber, SecondNumber)}")
elif programchoice == 3:
    print(f"Result: {Multiplication(FirstNumber, SecondNumber)}")
elif programchoice == 4:
    print(f"Result: {Division(FirstNumber, SecondNumber)}")