import math

number = 600851475143

def isPrime(num):
	for i in range(3, int(math.sqrt(num)), 2):
		if (num % i == 0):
			return False
	return True


for i in range( int(math.sqrt(number)) , 2 , -1):
	if(number % i == 0):
		if(isPrime(i)):
			print(i)
			break
			
