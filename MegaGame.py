import mysql.connector as ms
pwd=input("Enter your database's password:")
db=ms.connect(
host="localhost",
user="root",
passwd=pwd,
buffered=True
)
exec=True
def Get_One(Table):
    #Gets all the tables' details to store the High Scores after a game
    Columns="select column_name from information_schema.columns where table_schema='gamedb' and table_name=%s order by ordinal_position"
    GameCursor.execute(Columns,(Table,))
    Req=[]
    data=GameCursor.fetchall()
    for i in range(2,5):
        Req.extend(data[i])
    Req=Req[1:]
    return Req
def After_Game(Table,Name,plays,won):
   # Updates the new High Scores after a game has been played
    global Values
    for i in Values.get(Table):
        for j in i:
            if j[2]==Name:
                plays+=j[0]
                won+=j[1]
                j[0]=plays
                j[1]=won
                Table_Info=Get_One(Table)
                update="update "+str(Table)+" set "+'=%s,'.join(Table_Info)+"=%s where Name=%s"
                data=tuple(j)
                GameCursor.execute(update,data)
                db.commit()
        if len(i)>1:
           #Some games consider least score as the best while some consider most score as best
            if Table in ['sps','ttt']:
                L=sorted(i,reverse=True)
            elif Table in ['guess_no','hangman']:
                L=sorted(i)
            count=len(i)
            winning=[]
            playing=[]
            for k in L:
              winning.append([k[1],k[0]])
              playing.append(k[0])
            if Table in ['sps','ttt']:
                winnings=sorted(winning,reverse=True)
            elif Table in ['guess_no','hangman']:
                winnings=sorted(winning)
            w=[]
            [w.append(x) for x in winnings if x not in w]
            for l in w:
                if l[0]==0 and l[1]==0:
                    w.remove(l)
            stop=0
            for j in i:
              for  l in w:
                if stop<count:
                    if j[0]!=0 or j[1]!=0:
                        if l[1]==j[0] and l[0]==j[1]:
                            j.insert(0,w.index(l)+1)
                            stop+=1
                            if len(j)>4:
                                pass
                            else:
                                Table_Info=Get_One(Table)
                                update="update "+str(Table)+" set Position=%s,"+'=%s,'.join(Table_Info)+"=%s where Name=%s"
                                data=tuple(j)
                                GameCursor.execute(update,data)
                                db.commit()
                    elif j[0]==0 and j[1]==0:
                            j.insert(0,len(w)+1)
                            stop+=1
                            if len(j)>4:
                                pass
                            else:
                                Table_Info=Get_One(Table)
                                update="update "+str(Table)+" set Position=%s,"+'=%s,'.join(Table_Info)+"=%s where Name=%s"
                                data=tuple(j)
                                GameCursor.execute(update,data)
                                db.commit()
                else:
                    break
def Get(Table):
    #Updates information of an existing player after playing a game 
    Columns="select column_name from information_schema.columns where table_schema='gamedb' and table_name=%s order by ordinal_position"
    GameCursor.execute(Columns,(Table,))
    Req=[]
    data=GameCursor.fetchall()
    for i in range(2,5):
        Req.extend(data[i])
    Req=Req[1:]+Req[:1]
    get="Select "+','.join(Req)+" from " +str(Table)
    GameCursor.execute(get)
    d=GameCursor.fetchall()
    data=[]
    for i in d:
        data.append(list(i))
    return data      
def Select(Table):
    #Displays data from a selected table 
    select="select * from "+str(Table)
    GameCursor.execute(select)
def Show(Table,table_data):
    #Prints all the data in Tabular Form 
    data=GameCursor.fetchall()
    Name_Length=[table_data[0]]
    Play_Length=[table_data[1]]
    Score_Length=[table_data[2]]
    for rows in data:
      Name_Length.append(rows[2])
      Play_Length.append(str(rows[3]))
      Score_Length.append(str(rows[4]))
    Name_len=int((len(max(Name_Length,key=len))-len(table_data[0]))/2)
    Play_len=(len(max(Play_Length,key=len))-len(table_data[1]))
    Best_len=(len(max(Score_Length,key=len))-len(table_data[2]))
    column="Rank"+"|"+"User ID"+"|"+" "*Name_len+table_data[0]+" "*Name_len+"|"+table_data[1]+" "*Play_len+"|"+table_data[2]+" "*Best_len+"|"
    print(column)
    for rows in data:
        rowsone=[str(i) for i in rows]
        row="|".join(rowsone)
        Rank_len=int((len("Rank")-len(rowsone[0])))
        ID_len=int((len("User ID")-len(rowsone[1])))
        Name_len=int((len(max(Name_Length,key=len))-len(rowsone[2]))/2)
        Play_len=len(max(Play_Length,key=len))-len(rowsone[3])
        Best_len=len(max(Score_Length,key=len))-len(rowsone[4])
        row=" "*Rank_len+rowsone[0]+"|"+" "*ID_len+rowsone[1]+"|"+" "*Name_len+rowsone[2]+" "*Name_len+"|"+" "*Play_len+rowsone[3]+"|"+" "*Best_len+rowsone[4]+"|"
        print(row)
def Insert(Table,Name):
    #Adds information of a new player to the database 
    select="select * from "+str(Table)
    GameCursor.execute(select)
    data=GameCursor.fetchall()
    if len(data)==0:
        Into=("insert into "+str(Table)+"(Name) values (%s)")
        Data=(Name,)
        GameCursor.execute(Into, Data)
        db.commit()
    else: 
        Names=[]
        for i in data:
          Names.append(i[2])
        if Name in Names:
          return None
        else:     
          Into=("insert into "+str(Table)+"(Name) values (%s)")
          Data=(Name,)
          GameCursor.execute(Into, Data)
          db.commit()
def Game():
    """Contains all the games' databases and the user interface"""
    global Player_One,Player_Two
    def hangman():
        #Plays the game 'Hangman' 
        global Player_One,Player_Two,num_players
        if num_players==2:
            Players={1:Player_One,2:Player_Two}
            for i,j in Players.items(): 
                print(i,":",j)
            Player=int(input("Which player will play?(1,2):"))
            Name=Players[Player]
        if num_players==1:
            Name=Player_One
        from Hangman import wins,wrong,main
        main()
        After_Game('hangman',Name,wins,wrong)      

    def ttt():
         #Plays the game 'Tic Tac Toe'
        global Player_One,Player_Two
        from TicTacToe import Winning,Games,main
        main()
        Players={1:Player_One,2:Player_Two}
        After_Game('ttt',Player_One,Games[1],Winning[1])
        After_Game('ttt',Player_Two,Games[2],Winning[2])

    def sps():
         # """Plays the game 'Stone Paper Scissors'"""
        global Player_One,Player_Two,num_players
        if num_players==2:
            Players={1:Player_One,2:Player_Two}
            for i,j in Players.items():
                print(i,":",j)
            Player=int(input("Which player will play?(1,2):"))
            Name=Players[Player]
        if num_players==1:
            Name=Player_One
        from StonePaperScissors import wins,played,main
        main()
        After_Game('sps',Name,played,wins)
    def guess_no():
         # Plays the game 'Guess The Number'
        global Player_One,Player_Two,num_players
        if num_players==2:
            Players={1:Player_One,2:Player_Two}
            for i,j in Players.items():
                print(i,":",j)
            Player=int(input("Which player will play?(1,2):"))
            Name=Players[Player]
        if num_players==1:
            Name=Player_One
        from Guess_No import wins,wrong,main
        main()
        After_Game('guess_no',Name,wins,wrong)        



    if num_players==2:
        games={"a":{"Hangman":hangman},"b":{"Tic Tac Toe(2 Players)":ttt},"c":{"Stone Paper Scissors":sps},"d":{"Guess The Number":guess_no}}
        print("Which Game would you like to play?(a,b,c,d):")
        for choice in games:
            for Game_Name in games[choice]:
                print(choice+":"+Game_Name)
    elif num_players==1:
        games={"a":{"Hangman":hangman},"b":{"Stone Paper Scissors":sps},"c":{"Guess The Number":guess_no}}
        print("Which Game would you like to play?(a,b,c):")
        for choice in games:
            for Game_Name in games[choice]:
                print(choice+":"+Game_Name)        
    answer=input()
    if answer.lower() in games:
        for Game_Name in games[answer.lower()]:
            print("You chose "+Game_Name)
            funct=games[answer.lower()][Game_Name]()
            return funct
def Close():
    """Closes the Game"""
    global exec
    print("Okay!Closing the game...Byeee")
    exec=False
def High_Scores():
    """Displays the High Scores of Selected Game"""
    print("Which game\'s table would you like to see?:")
    games={"a":"Hangman","b":"Tic Tac Toe","c":"Stone Paper Scissors","d":"Guess The Number"}
    for choice,thing in games.items():
        print(choice+":"+thing)
    Ans=input("Enter Here:")
    if Ans.lower()=='a':
        select="select * from hangman order by position"
        GameCursor.execute(select)
        Show('hangman',["Name","Words Guessed","Wrong Letters"])
    elif Ans.lower()=='b':
        select="select * from ttt order by position"
        GameCursor.execute(select)
        Show('ttt',["Name","Games Played","Games Won"])
    elif Ans.lower()=='c':
        select="select * from sps order by position"
        GameCursor.execute(select)
        Show('sps',["Name","Games Played","Games Won"])
    elif Ans.lower()=='d':
        select="select * from guess_no order by position"
        GameCursor.execute(select)
        Show('guess_no',["Name","Numbers Guessed","Wrong Numbers"])
def Score():
    """Displays High Score of a Selected Player"""
    global num_players,Player_One,Player_Two
    games={"Hangman":{"hangman":["Name","Words Guessed","Wrong Letters"]},"Tic Tac Toe":{"ttt":["Name","Games Played","Games Won"]},"Stone Paper Scissors":{"sps":["Name","Games Played","Games Won"]},"Guess The Numbers":{"guess_no":["Name","Numbers Guessed","Wrong Numbers"]}}
    for choice in games:
        for Table in games[choice]:
            if num_players==1:
                select="select * from "+str(Table)+" where Name=%s order by position"
                names=(Player_One,)
            elif num_players==2:
                select="select * from "+str(Table)+" where Name=%s or Name=%s order by position"
                names=(Player_One,Player_Two)            
            GameCursor.execute(select,names)
            table_data=games[choice][Table]
            print("")
            print(choice)
            Show(Table,table_data)
def Delete():
    """Clears the whole Database"""
    global exec
    a=input("Are you sure about that?You won't be able to reaccess the data again.:O (y,n):")
    if a.lower() in ['y','yes']:
        delete="drop database gamedb"
        GameCursor.execute(delete)
        print("Database deleted!Closing the game...")
        exec=False
    elif a.lower() in ['n','no']:
        print("Okay. Your database is safe!:)")
        pass
    else:
        print("Invalid input.Closing game...")
        exec=False
#Main 
GameCursor=db.cursor()
GameCursor.execute('create database if not exists gamedb')
GameCursor.execute('use gamedb')
GameCursor.execute("CREATE TABLE if not exists hangman(Position int default 1,UserID int PRIMARY KEY AUTO_INCREMENT,Name varchar(20),Words_Guessed int default  0,Wrong_Letters int default  0)")
GameCursor.execute("CREATE TABLE if not exists sps(Position int default 1,UserID int PRIMARY KEY AUTO_INCREMENT,Name varchar(20),Games_Played int default  0,Games_Won int default  0)")
GameCursor.execute("CREATE TABLE if not exists guess_no(Position int default 1,UserID int PRIMARY KEY AUTO_INCREMENT,Name varchar(20),No_Guessed int default  0,Wrong_No int default  0)")
GameCursor.execute("CREATE TABLE if not exists ttt(Position int default 1,UserID int PRIMARY KEY AUTO_INCREMENT,Name varchar(20),TTT_Played int default  0,Wins int default  0)")
GameCursor.execute("Show tables")
tables=[]
for i in GameCursor:
    tables.append(i[0])
Values={"hangman":[],"sps":[],"guess_no":[],"ttt":[]}
print("How many players are playing?(1,2)")
num_players=int(input())
if num_players==1:
    Player_One=input("Enter your name!:")
    for table in tables:
        Insert(table,str(Player_One))
    print("Done")
elif num_players==2:
    Player_One=input("Enter 1st player\'s name:")
    Player_Two=input("Enter 2nd player\'s name:")
    for table in tables:
      Insert(table,str(Player_One))
      Insert(table,str(Player_Two))
    print("Done")
for table in tables:
    if table in Values:
        Values[table].append(Get(table))     
while exec:
    print("Welcome to the Mega Game")
    print("What would you like to do?")
    options={'a':'Play a Game','b':'Open High Scores Table','c':'Check your score in every game','d':'Close the Game','e':'Delete the Database'}
    things={'a':Game,'b':High_Scores,'c':Score,'d':Close,'e':Delete}
    for choice,thing in options.items():
        print(choice+":"+thing)
    Do=input("Enter a,b,c,d or e:")
    if Do.lower() in options:
        things.get(Do.lower())()
    else:
        print("Input not matched.:< Try Again!")

