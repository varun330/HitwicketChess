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

    def moveUp(self, p):
        if p.x==0:
            print("Out of Board Move")
        elif self.board[p.x-1][p.y].player==p.player:
            print("Own piece at Position")
        else:
            self.board[p.x-1][p.y]=self.board[p.x][p.y]
            p.x-=1
            self.flag = not self.flag

    def moveDown(self, p):
        if p.x==4:
            print("Out of Board Move")
        elif self.board[p.x+1][p.y].player==p.player:
            print("Own piece at Position")
        else:
            self.board[p.x+1][p.y]=self.board[p.x][p.y]
            p.x+=1
            self.flag = not self.flag

    def moveLeft(self, p):
        if p.y==0:
            print("Out of Board Move")
        elif self.board[p.x][p.y-1].player==p.player:
            print("Own piece at Position")
        else:
            self.board[p.x][p.y-1]=self.board[p.x][p.y]
            p.y-=1
            self.flag = not self.flag
    
    def moveRight(self, p):
        if p.y==4:
            print("Out of Board Move")
        elif self.board[p.x][p.y+1].player==p.player:
            print("Own piece at Position")
        else:
            self.board[p.x][p.y+1]=self.board[p.x][p.y]
            p.y+=1
            self.flag = not self.flag

a=input("Enter pieces for player 1 ").split()
A=[]
for i in a:
    if i=="h1":
        A.append(Piece())
# A=[Piece("A-"+a[i],1,4,i,0) for i in range(5)]
# a=input("Enter pieces for player 2 ").split()
# B=[Piece("B-"+a[i],2,0,i,0) for i in range(5)]
# del(a)
# game = Chess(A,B)
# game.printBoard()            