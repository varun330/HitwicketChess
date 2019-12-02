class Piece:
    def __init__(self, name, player, x, y, hero):
        self.name=name
        self.player=player
        self.x=x
        self.y=y
        self.hero=hero

class Chess:
    def __init__(self,A,B):
        self.board = [[Piece("-",0,0,0,0) for i in range(5)] for i in range(5)]
        self.board[0]=B
        self.board[4]=A
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

    def moveUp(self, p):
        if p.x==0:
            print("Out of Board Move")
        elif self.board[p.x-1][p.y].player==p.player:
            print("Own piece at Position")
        else:
            self.board[p.x-1][p.y]=self.board[p.x][p.y]
            self.board[p.x][p.y]=Piece("-",0,0,0,0)
            p.x-=1
            self.flag = not self.flag

    def moveDown(self, p):
        if p.x==4:
            print("Out of Board Move")
        elif self.board[p.x+1][p.y].player==p.player:
            print("Own piece at Position")
        else:
            self.board[p.x+1][p.y]=self.board[p.x][p.y]
            self.board[p.x][p.y]=Piece("-",0,0,0,0)
            p.x+=1
            self.flag = not self.flag

    def moveLeft(self, p):
        if p.y==0:
            print("Out of Board Move")
        elif self.board[p.x][p.y-1].player==p.player:
            print("Own piece at Position")
        else:
            self.board[p.x][p.y-1]=self.board[p.x][p.y]
            self.board[p.x][p.y]=Piece("-",0,0,0,0)
            p.y-=1
            self.flag = not self.flag
    
    def moveRight(self, p):
        if p.y==4:
            print("Out of Board Move")
        elif self.board[p.x][p.y+1].player==p.player:
            print("Own piece at Position")
        else:
            self.board[p.x][p.y+1]=self.board[p.x][p.y]
            self.board[p.x][p.y]=Piece("-",0,0,0,0)
            p.y+=1
            self.flag = not self.flag

    def countPlayerPieces(self,player):
        count=0
        for i in self.board:
            for j in i:
                if j.player=player:
                    count+=1
        return count

a=input("Enter pieces for player 1 ").split()
A=[]
for i in range(len(a)):
    h=0
    if a[i]=="h1":
        h=1
    elif a[i]=="h2":
        h=2
    elif a[i]=="h3":
        h=3
    A.append(Piece("A-"+a[i],1,4,i,h))

a=input("Enter pieces for player 1 ").split()
B=[]
for i in range(len(a)):
    h=0
    if a[i]=="h1":
        h=1
    elif a[i]=="h2":
        h=2
    elif a[i]=="h3":
        h=3
    B.append(Piece("B-"+a[i],2,0,i,h))

game = Chess(A,B)
game.printBoard()
while(True):
    if(game.flag):
        a = input("Player1 move: ").split(":")
        p = game.getPieceByName("A-"+a[0])
        if p==None:
            print("Piece not found")
        elif p.hero==0:
            if a[1]=="F":
                game.moveUp(p)
            elif a[1]=="B":
                game.moveDown(p)
            elif a[1]=="L":
                game.moveLeft(p)
            elif a[1]=="R":
                game.moveRight(p)
                
        if game.countPlayerPieces(2)==0:
            print("Player 1 wins")
            game.printBoard()
            break
    else:
        a = input("Player2 move: ").split(":")
        p = game.getPieceByName("B-"+a[0])
        if p==None:
            print("Piece not found")
        elif p.hero==0:
            if a[1]=="F":
                game.moveDown(p)
            elif a[1]=="B":
                game.moveUp(p)
            elif a[1]=="L":
                game.moveRight(p)
            elif a[1]=="R":
                game.moveLeft(p)

        if game.countPlayerPieces(1)==0:
            print("Player 2 wins")
            game.printBoard()
            break

    game.printBoard()    
    