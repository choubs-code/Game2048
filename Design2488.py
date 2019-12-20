from numpy import rot90
from random import choice
from random import randint
from random import seed
import time

BOARD_SIZE = 4

class game2488:
	def __init__(self):
		self.matrix = []
		for _ in range(BOARD_SIZE):
			self.matrix.append([0] * BOARD_SIZE)

		self.move_dict = {
			1: self.move_right,
			2: self.move_left,
			3: self.move_up,
			4: self.move_down
		}

		self.fill_random_two_position()
		print("Initial board:")
		print(self.matrix)

	def get_empty_cell(self):
		empty_cell_list = []
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if self.matrix[i][j] == 0:
					empty_cell_list.append([i,j])

		return empty_cell_list

	def fill_random_two_position(self):
		"""
		This method will fill random 2 position of our matrix.
		"""
		empty_cell_list = self.get_empty_cell()

		for _ in range(2):
			idx = randint(0,len(empty_cell_list) - 1)
			self.matrix[empty_cell_list[idx][0]][empty_cell_list[idx][1]] = 2
			del empty_cell_list[idx]

	def play_game(self):
		# Will decide break point here.
		while True:
			current_move = randint(0, 3)
			print("Current Move: {}".format(current_move))

			# Rotate and call move_left
			self.matrix = rot90(self.matrix, current_move)
			self.move_left()
			self.matrix = rot90(self.matrix, -current_move)

			# Add new value to board
			empty_cell_list = self.get_empty_cell()
			idx = randint(0,len(empty_cell_list) - 1)
			self.matrix[empty_cell_list[idx][0]][empty_cell_list[idx][1]] = 2

			print(self.matrix)
			time.sleep(5)


	# Move methods
	def move_right(self):
		pass

	def move_left(self):
		current_zero = -1
		for i in range(4):
			# Move all int to move_left
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
			current_zero = -1
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


