#AnimeGame 
import csv
import sys
def main():
   menu()


def menu():
    
    print("\n")
    print("\t      ------[ Welcome to Anime Fights ]----- ")
    print()

    choice = input("""
                   1: One Piece
                   2: Naruto Shippuden 
                   
               Please enter your choice: """)

    if choice == "1":
        print ("\n")
        import OnePiece 
    elif choice == "2":
        print ("\n")
        import Naruto
    else:
        choice == "0"
        sys.exit
   
    menu()


    
#the program is initiated,

main()
