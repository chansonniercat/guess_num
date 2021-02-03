import random

r = random.randint(1,5)
while True:
	num = input('Please guess a number: ')
	num = int(num)
	if num == r:
		print('Bingo')
		break
	elif num > r:
		print('Answer is smaller')
	elif num < r:
		print('Answer is larger')
