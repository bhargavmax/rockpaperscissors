from src import images
from src import inputoutput

def gamez(s):
    choiceU, choiceS = inputoutput.inpoot()
    if(choiceU==choiceS):
        print ("Draw")
    elif(choiceU==1) :
        if(choiceS==2):
            print ("Your choice : ")
            images.Rock()
            print ("System's choice : ")
            images.Paper()
            print ("--------------")
            print ("Rock gets beaten by Paper")
            print ("System gets a point")
            s.increase_sys()
        if(choiceS==3):
            print ("Your choice : ")
            images.Rock()
            print ("System's choice : ")
            images.Scissors()
            print ("Rock beats Scissors")
            print ("User gets a point")
            s.increase_user()
    elif(choiceU==2):
        if(choiceS==1):
            print ("Your choice : ")
            images.Paper()
            print ("System's choice : ")
            images.Rock()
            print ("--------------")
            print ("Paper beats Rock")
            print ("User gets a point")
            s.increase_user()
        if(choiceS==3):
            print ("Your choice : ")
            images.Paper()
            print ("System's choice : ")
            images.Scissors()
            print ("--------------")
            print ("Paper gets beaten by Scissors")
            print ("System gets a point")
            s.increase_sys()
    elif(choiceU==3):
        if(choiceS==1):
            print ("Your choice : ")
            images.Scissors()
            print ("System's choice : ")
            images.Rock()
            print ("--------------")
            print ("Scissors get beaten by Rock")
            print ("System gets a point")
            s.increase_sys()
        if(choiceS==2):
            print ("Your choice : ")
            images.Scissors()
            print ("System's choice : ")
            images.Paper()
            print ("--------------")
            print ("Scissors beat Paper")
            print ("User gets a point")
            s.increase_user()
    user, sys = s.return_scores()
    print ("User : ", user)
    print ("System : ", sys)
    return s
