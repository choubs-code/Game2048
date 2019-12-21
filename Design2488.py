from numpy import rot90
from random import choice
from random import randint
from random import seed
import time

GAME_MATRIX_SIZE = 4

MOVE_LEFT = 0
MOVE_UP = 1
MOVE_RIGHT = 2
MOVE_DOWN = 3
AUTO_PLAY = 8
QUIT_GAME = 9

class game2488:
	def __init__(self):
		# Possible moves values.
		self.possible_moves = [MOVE_LEFT, MOVE_UP, MOVE_RIGHT, MOVE_DOWN, AUTO_PLAY, QUIT_GAME]

		# Highest cell's value.
		self.highest_cell_value = 0

		# Possible next move during auto-play.
		self.possible_next_move = None

		# Number of empty cell present in matrix.
		self.num_empty_cell_present = 0

		# Score of the game.
		self.score = 0

		# Game matrix.
		self.matrix = []
		for _ in range(GAME_MATRIX_SIZE):
			self.matrix.append([0] * GAME_MATRIX_SIZE)

		# Start with 2 cell with 2 number in each
		self.__fill_random_n_position(num_cell=2)
		print(self.matrix)

	def __get_empty_cell(self):
		"""
		This function will return list of empty [row, col]
		"""
		self.num_empty_cell_present = 0
		empty_cell_list = []
		for i in range(GAME_MATRIX_SIZE):
			for j in range(GAME_MATRIX_SIZE):
				if self.matrix[i][j] == 0:
					self.num_empty_cell_present += 1
					empty_cell_list.append([i,j])

				if self.highest_cell_value < self.matrix[i][j]:
					self.highest_cell_value = self.matrix[i][j]

		return empty_cell_list

	def __fill_random_n_position(self, num_cell=1):
		"""
		Initialize number of cells mentioned in parameter
		num_cell value can only be 1 or 2
		Return values:
		False: Game finished.
		True: Game not over yet.
		"""
		empty_cell_list = self.__get_empty_cell()

		if self.__in_end_game_now():
			return False

		for _ in range(num_cell):
			# If no. of empty cell is present then continue
			if not self.num_empty_cell_present:
				continue

			# If no. of empty cell is only one than we can directly fill it.
			if self.num_empty_cell_present == 1:
				idx = 0
			else:
				idx = randint(0, self.num_empty_cell_present - 1)

			self.matrix[empty_cell_list[idx][0]][empty_cell_list[idx][1]] = choice([2,4])
			del empty_cell_list[idx]
			self.num_empty_cell_present -= 1

		return True

	def __in_end_game_now(self):
		"""
		Check for game status. Game can be continued in following cases:
			1. Matrix have empty cell(s).
			2. Any one of cell's left/right and just up/down cell have same value.
		Return values:
		True: Game finished, no possible moves remaining.
		False: Game not over yet.
		"""
		in_the_end_game = True

		# Check for case 2, if case 1 fails.
		if not self.num_empty_cell_present:
			for i in range(GAME_MATRIX_SIZE):
				for j in range(GAME_MATRIX_SIZE):
					# Comparing left/right cell values.
					if j < GAME_MATRIX_SIZE - 1:
						if self.matrix[i][j] == self.matrix[i][j + 1]:
							self.possible_next_move = 2
							in_the_end_game = False
					   		break

					# Comparing up/down cell values.
					if i < GAME_MATRIX_SIZE - 1:
					   	if self.matrix[i][j] == self.matrix[i + 1][j]:
					   		self.possible_next_move = 1
					   		in_the_end_game = False
					   		break
				if not in_the_end_game:
					break
		else:
			self.possible_next_move = None
			return False

		if in_the_end_game:
			self.possible_next_move = None

		return in_the_end_game

	def play_game(self, autoplay=False):
		autoplay_wait_time = 0
		while True:
			if not autoplay:
				self.possible_next_move = self.__get_input()
				if self.possible_next_move == 9:
					break
				elif self.possible_next_move == 8:
					autoplay = True
			else:
				if not self.possible_next_move:
					self.possible_next_move = randint(0, 3)
				autoplay_wait_time = 0
				print("Current Move: {}".format(self.possible_next_move))

			# Rotate counter clockwise
			self.matrix = rot90(self.matrix, self.possible_next_move)
			
			# Make move to left
			self.__move_each_cols_left()

			# Rotate clockwise to original
			self.matrix = rot90(self.matrix, -1 * self.possible_next_move)

			# Add new value to board
			if not self.__fill_random_n_position(num_cell=1):
				print("You played well!!!")
				print("Final score {}".format(self.score))
				print("Highest cell value: {}".format(self.highest_cell_value))
				break

			if self.highest_cell_value == 2048:
				print("You made it!!!")

			print(self.matrix)
			print("Total score {}".format(self.score))
			time.sleep(autoplay_wait_time)

	def __move_each_cols_left(self):
		"""
		Method to move all item to left as per game rule.
		"""
		for i in range(GAME_MATRIX_SIZE):
			position_available = 0
			last_number = 0
			for j in range(GAME_MATRIX_SIZE):
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

	def __get_input(self):
		while True:
			next_move = input("Please enter next move: "
							  "[0: Left, 1: Up, 2: Right, 3: Down, 8: Auto-play, 9: Quit]: ")
			if next_move not in self.possible_moves:
				continue
			else:
				return next_move


if __name__ == "__main__":
	objGame = game2488()
	objGame.play_game()


