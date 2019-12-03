from Pieces import *
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
    
