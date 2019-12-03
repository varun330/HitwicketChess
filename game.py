class Piece:
    def __init__(self, name, player, x, y):
        self.name = name
        self.player = player
        self.x = x
        self.y = y
    


class NormalPiece(Piece):
    def __init__(self, name, player, x, y):
        super().__init__(name, player, x, y)

    def __moveF(self, board):
        if self.x == 0:
            print("Out of Board Move")
        elif board.board[self.x-1][self.y].player==self.player:
            print("Own piece at Position")
        else:
            board.board[self.x-1][self.y]=board.board[self.x][self.y]
            board.board[self.x][self.y]=Piece("-",0,0,0)
            self.x-=1
            board.flag = not board.flag
    
    def __moveB(self,board):
        if self.x==board.n-1:
            print("Out of Board Move")
        elif board.board[self.x+1][self.y].player==self.player:
            print("Own piece at Position")
        else:
            board.board[self.x+1][self.y]=board.board[self.x][self.y]
            board.board[self.x][self.y]=Piece("-",0,0,0)
            self.x+=1
            board.flag = not board.flag

    def __moveL(self,board):
        if self.y==0:
            print("Out of Board Move")
        elif board.board[self.x][self.y-1].player==self.player:
            print("Own piece at Position")
        else:
            board.board[self.x][self.y-1]=board.board[self.x][self.y]
            board.board[self.x][self.y]=Piece("-",0,0,0)
            self.y-=1
            board.flag = not board.flag

    def __moveR(self,board):
         if self.y==board.n-1:
            print("Out of Board Move")
        elif board.board[self.x][self.y+1].player==self.player:
            print("Own piece at Position")
        else:
            board.board[self.x][self.y+1]=board.board[self.x][self.y]
            board.board[self.x][self.y]=Piece("-",0,0,0)
            self.y+=1
            board.flag = not board.flag

    def move(self,board,direction):
        if self.player==1:
            if direction=="F":
                self.__moveF(board)

            elif direction=="B":
                self.__moveB(board)
            
            elif direction=="L":
                self.__moveL(board)

            elif direction=="R":
               self.__moveR(board)
        else:
            if direction=="B":
                self.__moveF(board)

            elif direction=="F":
                self.__moveB(board)
            
            elif direction=="R":
                self.__moveL(board)

            elif direction=="L":
                self.__moveR(board)

class Hero1(Piece):
    def __init__(self, name, player, x, y):
        super().__init__(name, player, x, y)
    
    def __moveF(self, board):
        if self.x<=1:
            print("Out of Board Move")
        elif board.board[self.x-1][self.y].player==self.player or board.board[self.x-2][self.y].player==self.player:
            print("Own piece at Position")
        else:
            board.board[self.x-2][self.y]=board.board[self.x][self.y]
            board.board[self.x][self.y]=Piece("-",0,0,0)
            board.board[self.x-1][self.y]=Piece("-",0,0,0)
            self.x-=2
            board.flag = not board.flag
    
    def __moveB(self, board):
        if self.x>=board.n-2:
            print("Out of Board Move")
        elif board.board[self.x+1][self.y].player==self.player or board.board[self.x+2][self.y].player==self.player:
            print("Own piece at Position")
        else:
            board.board[self.x+2][self.y]=board.board[self.x][self.y]
            board.board[self.x][self.y]=Piece("-",0,0,0)
            board.board[self.x+1][self.y]=Piece("-",0,0,0)
            self.x+=2
            board.flag = not board.flag
        
    def __move

    def move(self,board,direction):
        if self.player==1:
            if direction=="F":
               self.__moveF(board)

            elif direction=="B":
                self.__moveB(board)

            elif direction=="L":
                if self.y<=1:
                    print("Out of Board Move")
                elif board.board[self.x][self.y-1].player==self.player or board.board[self.x][self.y-2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x][self.y-2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x][self.y-1]=Piece("-",0,0,0)
                    self.y-=2
                    board.flag = not board.flag

            elif direction=="R":
                if self.y>=board.n-2:
                    print("Out of Board Move")
                elif board.board[self.x][self.y+1].player==self.player or board.board[self.x][self.y+2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x][self.y+2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x][self.y+1]=Piece("-",0,0,0)
                    self.y+=2
                    board.flag = not board.flag
        else:
            if direction=="B":
               self.__moveF(board)

            elif direction=="F":
                self.__moveB(board)
            
            elif direction=="R":
                if self.y<=1:
                    print("Out of Board Move")
                elif board.board[self.x][self.y-1].player==self.player or board.board[self.x][self.y-2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x][self.y-2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x][self.y-1]=Piece("-",0,0,0)
                    self.y-=2
                    board.flag = not board.flag

            elif direction=="L":
                if self.y>=board.n-2:
                    print("Out of Board Move")
                elif board.board[self.x][self.y+1].player==self.player or board.board[self.x][self.y+2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x][self.y+2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x][self.y+1]=Piece("-",0,0,0)
                    self.y+=2
                    board.flag = not board.flag

class Hero2(Piece):
    def __init__(self, name, player, x, y):
        super().__init__(name,player,x,y)
    
    def move(self, board, direction):
        if self.player==1:
            if direction=="FR":
                if self.x<=1 or self.y>=board.n-2:
                    print("Out of Board Move")
                elif board.board[self.x-1][self.y+1].player==self.player or board.board[self.x-2][self.y+2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x-2][self.y+2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x-1][self.y+1]=Piece("-",0,0,0)
                    self.x-=2
                    self.y+=2
                    board.flag = not board.flag

            elif direction=="BR":
                if self.x>=board.n-2 or self.y>=board.n-2:
                    print("Out of Board Move")
                elif board.board[self.x+1][self.y+1].player==self.player or board.board[self.x+2][self.y+2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x+2][self.y+2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x+1][self.y+1]=Piece("-",0,0,0)
                    self.x+=2
                    self.y+=2
                    board.flag = not board.flag

            if direction=="FL":
                if self.x<=1 or self.y<=1:
                    print("Out of Board Move")
                elif board.board[self.x-1][self.y-1].player==self.player or board.board[self.x-2][self.y-2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x-2][self.y-2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x-1][self.y-1]=Piece("-",0,0,0)
                    self.x-=2
                    self.y-=2
                    board.flag = not board.flag

            elif direction=="BL":
                if self.x>=board.n-2 or self.y<=1:
                    print("Out of Board Move")
                elif board.board[self.x+1][self.y-1].player==self.player or board.board[self.x+2][self.y-2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x+2][self.y-2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x+1][self.y-1]=Piece("-",0,0,0)
                    self.x+=2
                    self.y-=2
                    board.flag = not board.flag
        else:
            if direction=="BL":
                if self.x<=1 or self.y>=board.n-2:
                    print("Out of Board Move")
                elif board.board[self.x-1][self.y+1].player==self.player or board.board[self.x-2][self.y+2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x-2][self.y+2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x-1][self.y+1]=Piece("-",0,0,0)
                    self.x-=2
                    self.y+=2
                    board.flag = not board.flag

            elif direction=="FL":
                if self.x>=board.n-2 or self.y>=board.n-2:
                    print("Out of Board Move")
                elif board.board[self.x+1][self.y+1].player==self.player or board.board[self.x+2][self.y+2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x+2][self.y+2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x+1][self.y+1]=Piece("-",0,0,0)
                    self.x+=2
                    self.y+=2
                    board.flag = not board.flag

            if direction=="BR":
                if self.x<=1 or self.y<=1:
                    print("Out of Board Move")
                elif board.board[self.x-1][self.y-1].player==self.player or board.board[self.x-2][self.y-2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x-2][self.y-2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x-1][self.y-1]=Piece("-",0,0,0)
                    self.x-=2
                    self.y-=2
                    board.flag = not board.flag

            elif direction=="FR":
                if self.x>=board.n-2 or self.y<=1:
                    print("Out of Board Move")
                elif board.board[self.x+1][self.y-1].player==self.player or board.board[self.x+2][self.y-2].player==self.player:
                    print("Own piece at Position")
                else:
                    board.board[self.x+2][self.y-2]=board.board[self.x][self.y]
                    board.board[self.x][self.y]=Piece("-",0,0,0)
                    board.board[self.x+1][self.y-1]=Piece("-",0,0,0)
                    self.x+=2
                    self.y-=2
                    board.flag = not board.flag

class Hero3(Piece):
    def __init__(self, name, player, x, y):
        super().__init__(name, player,x,y)
    
    def move(self,board,direction):
        if self.player==1:
            if direction=="FL":
                if self.x
            

class Chess:
    def __init__(self,n,A,B):
        self.n=n
        self.board = [[Piece("-",0,0,0) for i in range(n)] for i in range(n)]
        self.board[0]=B
        self.board[n-1]=A
        self.flag=True

    def getPieceByName(self,name):
        for i in self.board:
            for j in i:
                if j.name==name:
                    return j
        return None
    
    def printBoard(self):
        for i in self.board:
            line = ""
            for j in i:
                line+=" "+j.name+" "
            print(line)
        print("\n")

    def countPlayerPieces(self,player):
        count=0
        for i in self.board:
            for j in i:
                if j.player==player:
                    count+=1
        return count

a=input("Enter pieces for player 1 ").split()
A=[]
for i in range(len(a)):
    if a[i]=="h1":
        A.append(Hero1("A-"+a[i],1,len(a)-1,i))
    elif a[i]=="h2":
        A.append(Hero2("A-"+a[i],1,len(a)-1,i))
    elif a[i]=="h3":
        pass
    else:
        A.append(NormalPiece("A-"+a[i],1,len(a)-1,i))
    
    

a=input("Enter pieces for player 1 ").split()
B=[]
for i in range(len(a)):
    if a[i]=="h1":
        B.append(Hero1("B-"+a[i],2,0,i))
    elif a[i]=="h2":
        B.append(Hero2("B-"+a[i],2,0,i))
    elif a[i]=="h3":
        pass
    else:
        B.append(NormalPiece("B-"+a[i],2,0,i))
    

game = Chess(len(a),A,B)
game.printBoard()
while(True):
    if(game.flag):
        a = input("Player1 move: ").split(":")
        p = game.getPieceByName("A-"+a[0])
        if p==None:
            print("Piece not found")
        else:
            p.move(game,a[1])

        if game.countPlayerPieces(2)==0:
            print("Player 1 wins")
            game.printBoard()
            break
    else:
        a = input("Player2 move: ").split(":")
        p = game.getPieceByName("B-"+a[0])
        if p==None:
            print("Piece not found")
        else:
            p.move(game,a[1])
            
        if game.countPlayerPieces(1)==0:
            print("Player 2 wins")
            game.printBoard()
            break

    game.printBoard()    
    
