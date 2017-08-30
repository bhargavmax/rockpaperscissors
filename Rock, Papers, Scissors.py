from src import images
from src import thegame
from src import inputoutput


def main() :
    inputoutput.setozero()
    ch="y"
    while(ch=="y" or ch=="Y"):
        images.menu()
        thegame.gamez()
        ch=input("Would you like to continue? (Y/N)")
    return

main()
