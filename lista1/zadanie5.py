
# lista 1, zadanie 5
# Mikołaj Kowalik, 283476
def tabliczka(x1, x2, y1, y2):
	print('     ', end = '')
	for i in range(x1, x2+1):
		print( '{:5d}'.format(i), end = '' )
	print()
	for i in range(y1, y2+1):
		print( '{:5d}'.format(i) , end = '')
		for j in range(x1, x2+1):
			print( '{:5d}'.format( i*j ), end = '' )
		print()
	
print('Zadanie 5.')	
tabliczka(3, 5, 2, 4)


