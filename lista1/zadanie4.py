# lista 1, zadanie 4
# Mikołaj Kowalik, 283476

from math import ceil


def is_prime( x ):
	if x < 2 :
		return False
	if x == 2 :
		return True	
	for i in range( 2, ceil(x**0.5) + 1) :
		if x % i == 0 :
			return False
	return True 
	

def rozklad( n ) :
	# L to lista liczb pierwszych mniejszych od n/2 + 1, które ją dzielą
	L = [ i for i in range( 1,  ceil(n/2)+1 ) if is_prime(i) and n % i == 0]
	# jeśli L jest puste to znaczy, że n jest liczbą pierwszą
	if L == [] :
		return [ (n, 1) ]
	res = []
	for p in L :
		i = 1
		while n % (p ** i) == 0 :
			i = i + 1
		res.append( (p, i-1) )
	return res 
	
print( 'Zadanie 4.' )
print( rozklad( 756 ) )
