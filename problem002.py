sum = 2
limit = 4000000
current = 2
previous = 1
curentCalculated = 0

while(current < limit):
	currentCalculated = current + previous
	previous = current
	current = currentCalculated
	if(current % 2 == 0):
		sum += current

print(sum)
