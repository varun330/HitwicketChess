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
