wins=0
played=0
def Again():
    global played,wins
    print("Would you like to play again?(y,n)")
    play_again=input()
    if play_again.lower()=="y":
        print("Starting again!")
        main()
    elif play_again.lower()=="n":
        print("Okay!Bye Bye.")
        print("You won",wins,"out of ",played,"games.")
    else:
        print("You won",wins,"out of ",played,"games.")
        print("No Valid Output!Closing The Game.")
def main():
    global played,wins
    import random
    Game=['Stone','Paper','Scissors']
    Win={"Stone":"Scissors","Paper":"Stone","Scissors":"Paper"}
    C=random.randrange(3)
    Computer=Game[C]
    Player=input("Pick either 'Stone','Paper' or 'Scissors':")
    Player_output,Computer_output=Player.title(),Computer.title()
    if Player_output in Game and Computer_output in Game:
        print("Player's Output:",Player_output)
        print("Computer's Output:",Computer_output)
        played+=1
        if Win[Player_output]==Computer_output:
            print("Player wins")
            wins+=1
            Again()
        elif Win[Computer_output]==Player_output:
            print("Computer wins")
            Again()
        elif Player_output==Computer_output:
            print("It's a tie!")
            Again()
    else:
        print("Wrong Input!")
        main()
if __name__=='__main__':
    main()
