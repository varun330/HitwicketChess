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