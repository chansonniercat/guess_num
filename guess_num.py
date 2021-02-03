import random
start = input('Please enter the starting range: ')
end = input('Please enter the ending range: ')
start = int(start)
end = int(end)

r = random.randint(start,end)
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
	
