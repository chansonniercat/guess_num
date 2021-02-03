import random

r = random.randint(1,5)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('Please guess a number: ')
	num = int(num)
	print ('This is your', count,'guess.')
	if num == r:
		print('Bingo')
		break
	elif num > r:
		print('Answer is smaller')
	elif num < r:
		print('Answer is larger')
	
