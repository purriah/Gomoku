from board import Board
class Player:
	def __init__(self,color):
		self.color = color

	def move(self,board,x,y):
		board.config[x][y]=self.color
		print(board.toString())

	def win(self,board,pivot_x,pivot_y):
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y] == self.color) && (board[pivot_x-2][pivot_y] == self.color) && (board[pivot_x-3][pivot_y] == self.color) && (board[pivot_x-4][pivot_y] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y] == self.color) && (board[pivot_x-2][pivot_y] == self.color) && (board[pivot_x-3][pivot_y] == self.color) && (board[pivot_x+1][pivot_y] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y] == self.color) && (board[pivot_x-2][pivot_y] == self.color) && (board[pivot_x-3][pivot_y] == self.color) && (board[pivot_x-4][pivot_y] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y] == self.color) && (board[pivot_x-2][pivot_y] == self.color) && (board[pivot_x+1][pivot_y] == self.color) && (board[pivot_x+2][pivot_y] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y] == self.color) && (board[pivot_x+1][pivot_y] == self.color) && (board[pivot_x+2][pivot_y] == self.color) && (board[pivot_x+3][pivot_y] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x+1][pivot_y] == self.color) && (board[pivot_x+2][pivot_y] == self.color) && (board[pivot_x+3][pivot_y] == self.color) && (board[pivot_x+4][pivot_y] == self.color):
			return True

		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x][pivot_y-1] == self.color) && (board[pivot_x][pivot_y-2] == self.color) && (board[pivot_x][pivot_y-3] == self.color) && (board[pivot_x][pivot_y-4] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x][pivot_y-1] == self.color) && (board[pivot_x][pivot_y-2] == self.color) && (board[pivot_x][pivot_y-3] == self.color) && (board[pivot_x][pivot_y+1] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x][pivot_y-1] == self.color) && (board[pivot_x][pivot_y-2] == self.color) && (board[pivot_x][pivot_y-3] == self.color) && (board[pivot_x][pivot_y-4] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x][pivot_y-1] == self.color) && (board[pivot_x][pivot_y-2] == self.color) && (board[pivot_x][pivot_y+1] == self.color) && (board[pivot_x][pivot_y+2] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x][pivot_y-1] == self.color) && (board[pivot_x][pivot_y+1] == self.color) && (board[pivot_x][pivot_y+2] == self.color) && (board[pivot_x][pivot_y+3] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x][pivot_y+1] == self.color) && (board[pivot_x][pivot_y+2] == self.color) && (board[pivot_x][pivot_y+3] == self.color) && (board[pivot_x][pivot_y+4] == self.color):
			return True

		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y-1] == self.color) && (board[pivot_x-2][pivot_y-2] == self.color) && (board[pivot_x-3][pivot_y-3] == self.color) && (board[pivot_x-4][pivot_y-4] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y-1] == self.color) && (board[pivot_x-2][pivot_y-2] == self.color) && (board[pivot_x-3][pivot_y-3] == self.color) && (board[pivot_x+1][pivot_y+1] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y-1] == self.color) && (board[pivot_x-2][pivot_y-2] == self.color) && (board[pivot_x-3][pivot_y-3] == self.color) && (board[pivot_x-4][pivot_y-4] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y-1] == self.color) && (board[pivot_x-2][pivot_y-2] == self.color) && (board[pivot_x+1][pivot_y+1] == self.color) && (board[pivot_x+2][pivot_y+2] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y-1] == self.color) && (board[pivot_x+1][pivot_y+1] == self.color) && (board[pivot_x+2][pivot_y+2] == self.color) && (board[pivot_x+3][pivot_y+3] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x+1][pivot_y+1] == self.color) && (board[pivot_x+2][pivot_y+2] == self.color) && (board[pivot_x+3][pivot_y+3] == self.color) && (board[pivot_x+4][pivot_y+4] == self.color):
			return True

		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y+1] == self.color) && (board[pivot_x-2][pivot_y+2] == self.color) && (board[pivot_x-3][pivot_y+3] == self.color) && (board[pivot_x-4][pivot_y+4] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y+1] == self.color) && (board[pivot_x-2][pivot_y+2] == self.color) && (board[pivot_x-3][pivot_y+3] == self.color) && (board[pivot_x+1][pivot_y-1] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y+1] == self.color) && (board[pivot_x-2][pivot_y+2] == self.color) && (board[pivot_x-3][pivot_y+3] == self.color) && (board[pivot_x-4][pivot_y+4] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y+1] == self.color) && (board[pivot_x-2][pivot_y+2] == self.color) && (board[pivot_x+1][pivot_y-1] == self.color) && (board[pivot_x+2][pivot_y-2] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x-1][pivot_y+1] == self.color) && (board[pivot_x+1][pivot_y-1] == self.color) && (board[pivot_x+2][pivot_y-2] == self.color) && (board[pivot_x+3][pivot_y-3] == self.color):
			return True
		if (board[pivot_x][pivot_y] == self.color) && (board[pivot_x+1][pivot_y-1] == self.color) && (board[pivot_x+2][pivot_y-2] == self.color) && (board[pivot_x+3][pivot_y-3] == self.color) && (board[pivot_x+4][pivot_y-4] == self.color):
			return True

