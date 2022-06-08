Winning={1:0,2:0}
Games={1:0,2:0}
def main():
    global Winning,Games
    game=[[0,0,0],
          [0,0,0],
          [0,0,0]]
    def win(current_game):
        global wins,played
        def all_same(l):
            if l.count(l[0])==len(l) and l[0]!=0:
                return True
            else:
                return False
            
        #Horizontal
        for row in game:
            if all_same(row):
                print("Player",row[0],"is the winner horizontally")
                Winning[row[0]]+=0.5
                return True
                
        #Vertical
        for col in range(len(game)):
            vert=[]
            for row in game:
                vert.append(row[col])
            if all_same(vert):
                print("Player",vert[0],"is the winner vertically")
                Winning[vert[0]]+=0.5
                return True

        #Diagonal
        rows=reversed(range(len(game)))
        cols=range(len(game))
        diags=[]
        for col, row in zip(cols,rows):
            diags.append(game[row][col])
        if all_same(diags):
            print("Player",diags[0],"is the winner diagonally (/)")
            Winning[diags[0]]+=0.5
            return True
        diags=[]
        for ix in range(len(game)):
            diags.append(game[ix][ix])
        if all_same(diags):
            print("Player",diags[0],"is the winner diagonally (\\)")
            Winning[diags[0]]+=0.5
            return True

        
        return False
    #GameBoard
    def game_board(game_map,player=0,row=0,column=0,just_display=False):
        if game_map[row][column]!=0:
            print("This position is occupied!Please chose another")
            return game_map, False
        print("   0  1  2")
        if not just_display: 
            game_map[row][column]=player
        count=65
        for row in game_map:
            print(chr(count),row)
            count+=1
        return game_map, True
        

    #PlayScreen
    play=True
    players=[1,2]
    while play:
        game=[[0,0,0],
                [0,0,0],
                [0,0,0]]
        game_won=False
        game,_ =game_board(game,just_display=True)
        current_player=players[1]
        while not game_won:
            if current_player==players[0]:
                current_player=players[1]
            elif current_player==players[1]:
                current_player=players[0]
            print("Current Player=",current_player)
            played=False
            while not played:
                try:
                    column_choice=int(input("Which column would you like to play? (0,1,2):"))
                    row_choice=input("Which row would you like to play? (A,B,C):")
                    game,played=game_board(game,current_player,ord(row_choice)-65,column_choice)
                except:
                    print("Chose from the given values!")
                
            if win(game):
                game_won=True
                Games[1]+=1
                Games[2]+=1
                print(Winning,Games)
                again=input("The game is over, would you like to play again? (y/n): ")
                if again.lower()=="y":
                    print("restarting")
                elif again.lower()=="n":
                    play=False
                    print("Bye Bye")
                    break
                else:
                    print("Not a valid answer,closing the game!")
                    play=False
    win(game)
if __name__ == '__main__':
    main()