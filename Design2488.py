from numpy import rot90
from random import choice
from random import randint
from random import seed
import time

BOARD_SIZE = 4

class game2488:
	def __init__(self):
		self.score = 0
		self.matrix = []
		for _ in range(BOARD_SIZE):
			self.matrix.append([0] * BOARD_SIZE)

		self.fill_random_n_position(positions=2)
		print("Initial board:")

	def get_empty_cell(self):
		empty_cell_list = []
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if self.matrix[i][j] == 0:
					empty_cell_list.append([i,j])

		return empty_cell_list

	def fill_random_n_position(self, positions=1):
		empty_cell_list = self.get_empty_cell()

		for _ in range(positions):
			idx = randint(0,len(empty_cell_list) - 1)
			self.matrix[empty_cell_list[idx][0]][empty_cell_list[idx][1]] = 2
			del empty_cell_list[idx]

	def play_game(self):
		print(self.matrix)
		# Will decide break point here.
		while True:
			current_move = randint(0, 3)
			print("Current Move: {}".format(current_move))

			# Rotate counter clockwise
			self.matrix = rot90(self.matrix, current_move)
			
			# Make move
			self.move_left()

			# Rotate clockwise
			self.matrix = rot90(self.matrix, -1 * current_move)

			# Add new value to board
			self.fill_random_n_position(positions=1)

			print(self.matrix)
			print("Total score {}".format(self.score))
			time.sleep(5)

	def move_left(self):
		current_zero = -1
		for i in range(4):
			position_available = 0
			last_number = 0
			for j in range(4):
				if self.matrix[i][j]:
					if not last_number:
						last_number = self.matrix[i][j]
						self.matrix[i][j] = 0
					else:
						if self.matrix[i][j] == last_number:
							self.matrix[i][j] = 0
							self.matrix[i][position_available] = \
								2 * last_number
							self.score += self.matrix[i][position_available]
							last_number = 0
							position_available += 1
						else:
							self.matrix[i][position_available] = last_number
							position_available += 1
							last_number = self.matrix[i][j]
							self.matrix[i][j] = 0

			if last_number:
				self.matrix[i][position_available] = last_number

objGame = game2488()
objGame.play_game()


