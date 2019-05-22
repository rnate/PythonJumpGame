class JumpGame:
	def __init__(self):
		self.steps = 0
		self.jump = 0
		self.level = 1
		self.score = 0
		self.runGame = True
		
		self.StartGame()

	def PrintPlayer(self):
		if self.jump > 0:
			person = ["O", "|-", "L\n"]
			print("\n\n\n\n\n\n\n\n\n\n\n\n")
		else:
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
			person = ["O", "|-", "L"]
		
		print(person[0])
		print(person[1])
		print(person[2], end="")
			
	def PrintObstacle(self):
		print("X".rjust(37 - self.steps))
		
	def PrintLevel(self):
		print("Level: " + str(self.level), end="")
		
	def PrintScore(self):
		print("Score: ".rjust(26) + (str(self.score)))

	def CheckJump(self, msvcrt):
		if msvcrt.kbhit() and ord(msvcrt.getch()) == 32:
			self.jump = 2
			
			if self.level <= 8:
				self.jump = 10 - self.level
		
		self.PrintPlayer()
		self.PrintObstacle()
		
	def Logic(self):
		if self.jump > 0:
			self.jump = self.jump - 1

		if self.steps >= 36 and self.jump <= 0:
			self.runGame = False
			self.level = self.level - 1
		elif self.steps > 35:
			self.steps = 0
			self.level = self.level + 1
		else:
			self.score = self.score + 1
			self.steps = self.steps + 1

	def RestartGame(self):
		if (input("Game over! Try again? (y/n)").lower() == "y"):
			JumpGame().StartGame()
	
	def StartGame(self):
		import os
		import time
		import msvcrt
		
		os.system("mode con:cols=40 lines=20")
		
		while self.runGame:
			self.PrintLevel()
			self.PrintScore()
			self.Logic()
			self.CheckJump(msvcrt)
			
			time.sleep(.04)
			
			if self.runGame:
				os.system("cls")
			else:
				self.RestartGame()

JumpGame().StartGame()