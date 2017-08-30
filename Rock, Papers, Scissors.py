from src import images
from src import thegame
from src import inputoutput


def main() :
    s = inputoutput.scoreBoard()
    ch="y"
    while(ch=="y" or ch=="Y"):
        images.menu()
        thegame.gamez(s)
        ch=input("Would you like to continue? (Y/N)")
    return

main()
