from board import Board
from player import Player

class Gomoku:
	def __init__(self):
		self.player1 = Player(1)
		self.player2 = Player(2)
		self.board = Board()

	#self is object itself (in this case gomoku)
	#capitalize objects and classes
	def play(self):
		while True:
			turn_x = raw_input("Player 1 turn x: ")	
			turn_y = raw_input("Player 1 turn y: ")
			
			while not (self.player1.check_legal(self.board,int(turn_x),int(turn_y))):
				turn_x = raw_input("Player 1 turn x: ")	
				turn_y = raw_input("Player 1 turn y: ")
			self.player1.move(self.board,int(turn_x),int(turn_y))
			
			if self.player1.win(self.board,int(turn_x),int(turn_y)):
				print("Player 1 wins")
				return
			
			turn_x = raw_input("Player 2 turn x: ")	
			turn_y = raw_input("Player 2 turn y: ")

			while not (self.player2.check_legal(self.board,int(turn_x),int(turn_y))):
				turn_x = raw_input("Player 2 turn x: ")	
				turn_y = raw_input("Player 2 turn y: ")
			self.player2.move(self.board,int(turn_x),int(turn_y))
			
			if self.player2.win(self.board,int(turn_x),int(turn_y)):
				print("Player 2 wins")
				return

game = Gomoku()
game.play()

