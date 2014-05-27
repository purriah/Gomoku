from board import Board
class Player:
	def __init__(self,color):
		self.color = color

	def move(self,board,x,y):
		board.config[x][y]=self.color
		print(board.toString())

	def check_legal(self,board,x,y):
		
		if x>15 or x<0:
			
			return False
		if y>15 or y<0:
			
			return False
		if board.config[x][y] !=0:
			
			return False
		
		return True

	def win(self,board,pivot_x,pivot_y):

		return self.check_horiz(board,pivot_x,pivot_y) or self.check_vert(board,pivot_x,pivot_y) or self.check_diag1(board,pivot_x,pivot_y) or self.check_diag2(board,pivot_x,pivot_y)


	def check_horiz(self,board,pivot_x,pivot_y):
		if (pivot_x-4)>=0:
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y] == self.color) and (board.config[pivot_x-2][pivot_y] == self.color) and (board.config[pivot_x-3][pivot_y] == self.color) and (board.config[pivot_x-4][pivot_y] == self.color):
				return True
		if (pivot_x-3>=0 and pivot_x+1<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y] == self.color) and (board.config[pivot_x-2][pivot_y] == self.color) and (board.config[pivot_x-3][pivot_y] == self.color) and (board.config[pivot_x+1][pivot_y] == self.color):
				return True
		if (pivot_x-2>=0 and pivot_x+2<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y] == self.color) and (board.config[pivot_x-2][pivot_y] == self.color) and (board.config[pivot_x+1][pivot_y] == self.color) and (board.config[pivot_x+2][pivot_y] == self.color):
				return True
		if (pivot_x-1>=0 and pivot_x+3<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y] == self.color) and (board.config[pivot_x+1][pivot_y] == self.color) and (board.config[pivot_x+2][pivot_y] == self.color) and (board.config[pivot_x+3][pivot_y] == self.color):
				return True
		if (pivot_x+4<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x+1][pivot_y] == self.color) and (board.config[pivot_x+2][pivot_y] == self.color) and (board.config[pivot_x+3][pivot_y] == self.color) and (board.config[pivot_x+4][pivot_y] == self.color):
				return True
	
	def check_vert(self,board,pivot_x,pivot_y):
		if (pivot_y-4)>=0:
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x][pivot_y-1] == self.color) and (board.config[pivot_x][pivot_y-2] == self.color) and (board.config[pivot_x][pivot_y-3] == self.color) and (board.config[pivot_x][pivot_y-4] == self.color):
				return True
		if (pivot_y-3>=0 and pivot_y+1<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x][pivot_y-1] == self.color) and (board.config[pivot_x][pivot_y-2] == self.color) and (board.config[pivot_x][pivot_y-3] == self.color) and (board.config[pivot_x][pivot_y+1] == self.color):
				return True
		if (pivot_x-2>=0 and pivot_y+2<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x][pivot_y-1] == self.color) and (board.config[pivot_x][pivot_y-2] == self.color) and (board.config[pivot_x][pivot_y+1] == self.color) and (board.config[pivot_x][pivot_y+2] == self.color):
				return True
		if (pivot_y-1>=0 and pivot_y+3<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x][pivot_y-1] == self.color) and (board.config[pivot_x][pivot_y+1] == self.color) and (board.config[pivot_x][pivot_y+2] == self.color) and (board.config[pivot_x][pivot_y+3] == self.color):
				return True
		if (pivot_y+4<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x][pivot_y+1] == self.color) and (board.config[pivot_x][pivot_y+2] == self.color) and (board.config[pivot_x][pivot_y+3] == self.color) and (board.config[pivot_x][pivot_y+4] == self.color):
				return True
	
	def check_diag1(self,board,pivot_x,pivot_y):
		if (pivot_x-4>=0 and pivot_y-4>=0):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y-1] == self.color) and (board.config[pivot_x-2][pivot_y-2] == self.color) and (board.config[pivot_x-3][pivot_y-3] == self.color) and (board.config[pivot_x-4][pivot_y-4] == self.color):
				return True
		if (pivot_x-3>=0 and pivot_y-3>=0 and pivot_x+1 <15 and pivot_y+1 <15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y-1] == self.color) and (board.config[pivot_x-2][pivot_y-2] == self.color) and (board.config[pivot_x-3][pivot_y-3] == self.color) and (board.config[pivot_x+1][pivot_y+1] == self.color):
				return True
		if (pivot_x-2>=0 and pivot_y-2>=0 and pivot_x+2<15 and pivot_y+2 <15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y-1] == self.color) and (board.config[pivot_x-2][pivot_y-2] == self.color) and (board.config[pivot_x+1][pivot_y+1] == self.color) and (board.config[pivot_x+2][pivot_y+2] == self.color):
				return True

		if (pivot_x-1>=0 and pivot_y-1>=0 and pivot_x+3 <15 and pivot_y+3 <15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y-1] == self.color) and (board.config[pivot_x+1][pivot_y+1] == self.color) and (board.config[pivot_x+2][pivot_y+2] == self.color) and (board.config[pivot_x+3][pivot_y+3] == self.color):
				return True
		if (pivot_x+4<15 and pivot_y+4<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x+1][pivot_y+1] == self.color) and (board.config[pivot_x+2][pivot_y+2] == self.color) and (board.config[pivot_x+3][pivot_y+3] == self.color) and (board.config[pivot_x+4][pivot_y+4] == self.color):
				return True
	
	def check_diag2(self,board,pivot_x,pivot_y):
		if (pivot_x-4>=0 and pivot_y+4<15):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y+1] == self.color) and (board.config[pivot_x-2][pivot_y+2] == self.color) and (board.config[pivot_x-3][pivot_y+3] == self.color) and (board.config[pivot_x-4][pivot_y+4] == self.color):
				return True

		if (pivot_x-3>=0 and pivot_y+3<15 and pivot_x+1 <15 and pivot_y-1 >=0):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y+1] == self.color) and (board.config[pivot_x-2][pivot_y+2] == self.color) and (board.config[pivot_x-3][pivot_y+3] == self.color) and (board.config[pivot_x+1][pivot_y-1] == self.color):
				return True

		if (pivot_x-2>=0 and pivot_y+2<15 and pivot_x+2<15 and pivot_y-2 >=0):
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y+1] == self.color) and (board.config[pivot_x-2][pivot_y+2] == self.color) and (board.config[pivot_x+1][pivot_y-1] == self.color) and (board.config[pivot_x+2][pivot_y-2] == self.color):
				return True

		if (pivot_x-1>=0 and pivot_y+1<15 and pivot_x+3 <15 and pivot_y-3 >=0):

			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x-1][pivot_y+1] == self.color) and (board.config[pivot_x+1][pivot_y-1] == self.color) and (board.config[pivot_x+2][pivot_y-2] == self.color) and (board.config[pivot_x+3][pivot_y-3] == self.color):
				return True

		if (pivot_x+4<15 and pivot_y-4>=0):
			
			if (board.config[pivot_x][pivot_y] == self.color) and (board.config[pivot_x+1][pivot_y-1] == self.color) and (board.config[pivot_x+2][pivot_y-2] == self.color) and (board.config[pivot_x+3][pivot_y-3] == self.color) and (board.config[pivot_x+4][pivot_y-4] == self.color):
				return True



