from random import seed
from random import choice
from random import randint

class game2488:
	def __init__(self):
		self.matrix = []
		for _ in range(4):
			self.matrix.append([0]*4)

		self.move_dict = {
			1: self.move_right,
			2: self.move_left,
			3: self.move_up,
			4: self.move_down
		}

		self.fill_random_two_position()

	def fill_random_two_position(self):
		"""
		This method will fill random 2 position of our matrix.
		"""
		for _ in range(2):
			i = randint(0,3)
			j = randint(0,3)
			self.matrix[i][j] = choice([2,4])

	def play_game(self):
		# Will decide break point here.
		while True:
			current_move = randint(1,4)
			self.move_dict[current_move]()
			# Get the cell left in matrix
			# If cell left is one and matrix before current_move 
			# and after move are same then we will end the game

	def get_cell_left(self):
		pass

	# Move methods
	def move_right(self):
		pass


	def move_left(self):
		for i in range(4):
			# Move all int to left
			for j in range(4):
				if self.matrix[i][j] == 0 and current_zero == -1:
					current_zero = j
					continue
				
				if self.matrix[i][j] != 0:
					self.matrix[i][j], self.matrix[i][current_zero] = \
						self.matrix[i][current_zero], self.matrix[i][j]
					current_zero += 1

			# Add equal int
			for j in range(3):
				if self.matrix[i][j] == self.matrix[i][j + 1]:
					self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][j + 1]
					self.matrix[i][j + 1] = 0

			# Move all int to left
			for j in range(4):
				if self.matrix[i][j] == 0 and current_zero == -1:
					current_zero = j
					continue
				
				if self.matrix[i][j] != 0:
					self.matrix[i][j], self.matrix[i][current_zero] = \
						self.matrix[i][current_zero], self.matrix[i][j]
					current_zero += 1

	def move_up(self):
		pass

	def move_down(self):
		pass



objGame = game2488()
objGame.play_game()


