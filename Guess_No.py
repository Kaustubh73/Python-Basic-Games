import random
wins=0
wrong=0
def main():
    global wins,wrong
    a=random.randint(0,21)
    try:
        b=int(input("Guess a number generated between 0 and 20:"))
    except:
        print("Something went wrong.Did you not enter a integer?")
        main()
    i=1
    current_wrong=0
    
    
    while i==1:
        if b in range(21): 
            if b>a:
                try:
                    b=int(input("Lower!:"))
                except:
                    print("Something went wrong.Did you not enter a integer?")
                    main()
                current_wrong+=1
                wrong+=1
            elif b<a:
                try:
                    b=int(input("Higher!:"))
                except:
                    print("Something went wrong.Did you not enter a integer?")
                    main()
                current_wrong+=1
                wrong+=1
            elif b==a:
                print("That's the number!")
                current_wrong+=1
                print("You guessed it after",current_wrong,"tries")
                wins+=1
                Ans=input("Would you like to play again? (y,n):")
                if Ans.lower()=='y':
                    print("Starting again!")
                    main()
                elif Ans.lower()=='n':
                    print("Okay!Bye Bye")
                else:
                    print("Invalid Output!Closing Game....")
                break
        else:
            print(b,"is not between 0 and 20!")
            b=int(input("Please enter another number:"))
if __name__=='__main__':
    main()