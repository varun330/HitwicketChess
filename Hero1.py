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
