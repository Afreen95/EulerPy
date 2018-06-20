import math 

def is_prime(n):
	if n % 2 == 0 : return False
	i = 3
	while (i < math.sqrt(n) + 1):
		if n % i == 0 : return False
		i += 2
	return True
	

def nth_prime(n):
	prime = 2 
	count = 1
	i = 3
	while (count < n):
		if(is_prime(i)):
			prime = i
			count += 1
		i += 2
	return prime	


print(nth_prime(10001))