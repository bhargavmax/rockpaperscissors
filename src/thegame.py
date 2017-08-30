from src import images
from src import inputoutput

def gamez():
    inputoutput.inpoot()
    if(inputoutput.choiceU==inputoutput.choiceS):
        print ("Draw")
    elif(inputoutput.choiceU==1) :
        if(inputoutput.choiceS==2):
            print ("Your choice : ")
            images.Rock()
            print ("System's choice : ")
            images.Paper()
            print ("--------------")
            print ("Rock gets beaten by Paper")
            print ("System gets a point")
            inputoutput.sys+=1
        if(inputoutput.choiceS==3):
            print ("Your choice : ")
            images.Rock()
            print ("System's choice : ")
            images.Scissors()
            print ("Rock beats Scissors")
            print ("User gets a point")
            inputoutput.user+=1
    elif(inputoutput.choiceU==2):
        if(inputoutput.choiceS==1):
            print ("Your choice : ")
            images.Paper()
            print ("System's choice : ")
            images.Rock()
            print ("--------------")
            print ("Paper beats Rock")
            print ("User gets a point")
            inputoutput.user+=1
        if(inputoutput.choiceS==3):
            print ("Your choice : ")
            images.Paper()
            print ("System's choice : ")
            images.Scissors()
            print ("--------------")
            print ("Paper gets beaten by Scissors")
            print ("System gets a point")
            inputoutput.sys+=1
    elif(inputoutput.choiceU==3):
        if(inputoutput.choiceS==1):
            print ("Your choice : ")
            images.Scissors()
            print ("System's choice : ")
            images.Rock()
            print ("--------------")
            print ("Scissors get beaten by Rock")
            print ("System gets a point")
            inputoutput.sys+=1
        if(inputoutput.choiceS==2):
            print ("Your choice : ")
            images.Scissors()
            print ("System's choice : ")
            images.Paper()
            print ("--------------")
            print ("Scissors beat Paper")
            print ("User gets a point")
            inputoutput.user+=1
    print ("User : ",inputoutput.user)
    print ("System : ",inputoutput.sys)
