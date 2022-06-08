import random
Fruits =["apple","banana","mango","strawberry","orange","grape","pineapple","apricot","lemon","coconut","watermelon","cherry","papaya","berry","peach","lychee","muskmelon","acerola","blackberry","blueberry","avocado",]
Applauds=["Good Job!","Correct!","Keep Going"]
Try=["Try Again","Wrong Answer","You Bad"]
wins=0
wrong=0
def Word(Guess,Enter=False):
    global word_guess
    global wrong,current_wrong
    global word
    global word_length
    if Enter:
        if Guess in word:
            new=""
            print(random.choice(Applauds))
            for i in range(word_length):
                if Guess==word[i]:
                    new+=word[i]
                else:
                    new+=word_guess[i]
            print(new)
            word_guess=new
        else:
            print(random.choice(Try))
            print(word_guess)
            wrong+=1
            current_wrong+=1
    else:
        print(word_guess)
def main():
    global word_guess
    global word
    global word_length
    global wins
    global wrong,current_wrong
    global scores
    current_wrong=0
    word=random.choice(Fruits)
    picked=[]
    picked.append(Fruits.pop(Fruits.index(word)))
    word_length=len(word)
    word_guess="-"*word_length
    max_wrong=word_length+2
    Word("Nothing")
    print("\nGuess the word!HINT:Fruit")
    Chance=1
    used=[]
    while current_wrong<=max_wrong and word_guess!=word:
        print("The word has",word_length,"Letters")
        print("You have",str(max_wrong-current_wrong),"chances")
        a=input("Guess No."+str(Chance)+":")
        if a in used:
            print(a,"has already been picked!Guess again")
        elif len(a)>1:
            print("Enter one letter at a time! :D")
        if not a.strip():
            print("Enter something! :(")
        else:
            used.append(a)
            Word(a,Enter=True)
        Chance+=1
    else:
        if word_guess==word:
            print("You have successfully guessed the word",word,"with",current_wrong,"wrong answers!")
            wins+=1
        else:
            print("You lost!The word was",word)
        Y_or_N=input("Do you wish to continue to the next word?:")
        if Y_or_N.lower() in ["yes","y"]:
            main()
        else:
            print("You won",wins,"Game!")
            print("Thanks for Playing")
if __name__=='__main__':
    main()

