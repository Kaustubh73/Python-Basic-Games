import random as rdm
def die():
    a=rdm.randint(1,6)
    print("The die has rolled",a)
    b=input("Do you want to roll again?(y/n)\n")
    if b.lower()=="y":
        die()
    else:
        print("Okay!Thanks for playing")
print("Welcome to the Dice Rolling Simulator")
c=input("Would you like to roll the dice?(y/n)\n")
if c.lower()=="y":
    die()
else:
    print("Thank you")       
