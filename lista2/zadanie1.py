class Wyrazenie:
	""" Klasa Wyrażenie """
	def oblicz(self, zmienne):
		pass

class Stala( Wyrazenie ):
	def oblicz(self, zmienne):
		return self.value
		
	def __init__(self, val):
		self.value = val
		
	def __str__(self):
		return str( self.value )
		

class Zmienna( Wyrazenie ):
	def oblicz(self, zmienne):
		return zmienne[self.label]
		
	def lbl(self):
		return self.label
	
	def __init__ (self, label):
		self.label = label
		
	def __str__(self):
		return str( self.label )
		
class Operator1Arg( Wyrazenie ):
	pass
	
class UnaryMinus( Operator1Arg ):
	def __init__(self, a):
		self.left = a
		
	def oblicz(self, zmienne):
		return -self.left.oblicz(zmienne)
		
	def __str__(self):
		return   "-" + str( self.left )
		
class Operator2Arg( Operator1Arg ):
	pass
	
class Dodaj( Operator2Arg ):
	def __init__(self, a, b):
		self.left = a
		self.right = b
		
	def oblicz(self, zmienne):
		return self.left.oblicz(zmienne) + self.right.oblicz(zmienne)
		
	def __str__(self):
		return  " ( " + str( self.left ) + " + " + str( self.right ) + " ) "
	
class Odejmij( Operator2Arg ):
	def __init__(self, a, b):
		self.left = a
		self.right = b
		
	def oblicz(self, zmienne):
		return self.left.oblicz(zmienne) - self.right.oblicz(zmienne)
		
	def __str__(self):
		return " ( " + str( self.left ) + " - " + str( self.right ) + " ) "
	
class Razy( Operator2Arg ):
	def __init__(self, a, b):
		self.left = a
		self.right = b
		
	def oblicz(self, zmienne):
		return self.left.oblicz(zmienne) * self.right.oblicz(zmienne)
		
	def __str__(self):
		return " ( " + str( self.left ) + " * " + str( self.right ) + " ) "
	
class Podziel( Operator2Arg ):
	def __init__(self, a, b):
		self.left = a
		self.right = b
		
	def oblicz(self, zmienne):
		mianownik = self.right.oblicz(zmienne)
		if mianownik == 0:
			raise ZeroDivisionError
			
		return self.left.oblicz(zmienne) / mianownik
			
	def __str__(self):
		return " ( " +str( self.left ) + " * " + str( self.right ) + " ) "
		
		
class LessThan( Wyrazenie ):
	def __init__(self, a, b):
		self.left = a
		self.right = b
		
	def oblicz(self, zmienne):
		
		if self.left.oblicz() < self.right.oblicz() :
			return 1
		else :
			return 0
			
	def __str__(self):
		return  str( self.left ) + " < " + str( self.right )
		
class LessEqualThan( Wyrazenie ):
	def __init__(self, a, b):
		self.left = a
		self.right = b
		
	def oblicz(self, zmienne):
		
		if self.left.oblicz(zmienne) <= self.right.oblicz(zmienne) :
			return 1
		else :
			return 0
			
	def __str__(self):
		return  str( self.left ) + " <= " + str( self.right )
		
class Equal( Wyrazenie ):
	def __init__(self, a, b):
		self.left = a
		self.right = b
		
	def oblicz(self, zmienne):
		
		if self.left.oblicz() == self.right.oblicz() :
			return 1
		else :
			return 0
			
	def __str__(self):
		return  str( self.left ) + " == " + str( self.right )
		

		
class Instrukcja:
	"""klasa instrukcji"""
	def wykonaj(self, zmienne):
		pass
		
class InstrukcjaWarunkowa( Instrukcja ):

	def __init__(self, wyr, ins):
		self.exp = wyr
		self.ins = ins
		
	def wykonaj(self, zmienne):
		if self.exp.oblicz( zmienne ) :
			return self.ins.wykonaj( zmienne )
		else:
			return zmienne
	
	def __str__(self):
		return  "if( "+str(self.exp)+" ){\n"+str(self.ins)+"\n}"

			
		
class ZlozInstrukcje( Instrukcja ):
	
	def __init__ ( self, leftIns, rightIns):
		self.leftIns = leftIns
		self.rightIns = rightIns
		
	def wykonaj(self, zmienne):
		z = self.leftIns.wykonaj( zmienne )
		return self.rightIns.wykonaj( z )
		
	def __str__(self):
		return  str(self.leftIns)+"\n"+str(self.rightIns)+"\n"
	
	
class InstrukcjaAssign( Instrukcja ):
	def __init__ (self, zmienna, doObliczenia ):
		self.etykieta = zmienna.lbl()
		self.right = doObliczenia
		
	def wykonaj(self, zmienne):
		zmienne[ self.etykieta ] = self.right.oblicz( zmienne )
		return zmienne
	
	def __str__(self):
		return  str( self.etykieta ) + " = " + str( self.right )
	
		
class forLoop( Instrukcja ):
	def __init__ ( self, inicjalizacja, warunek, inkrementacja, instrukcje ):
		self.init = inicjalizacja
		self.cond = warunek
		self.incr = inkrementacja
		self.body = instrukcje
		
	def wykonaj(self, zmienne):
		z = self.init.wykonaj(zmienne)
		while self.cond.oblicz( z ) :
			z = self.body.wykonaj(z)
			z = self.incr.wykonaj(z)
		return z
		
	def __str__(self):
		return  "for( "+str(self.init)+", "+ str(self.cond) + ", " +str(self.incr) + "){\n"+str(self.body)+"\n}"
			
			

	
print( Razy(Dodaj(Zmienna("x"), Stala(2)), Zmienna("y")) )	
print( Razy(Dodaj(Zmienna("x"), Stala(2)), Zmienna("y")).oblicz({ "x" : 2, "y" : 3 } ) )

print("\n\n")
#program suma od 0 do 10

print(	
	 	ZlozInstrukcje( 	InstrukcjaAssign( Zmienna("sum"), Stala(0) ), 
	 						forLoop( 	InstrukcjaAssign( Zmienna("i"), Stala(0) ), 
	 									LessEqualThan( Zmienna("i"), Stala(10) ), 
	 									InstrukcjaAssign( 	Zmienna("i"), 
	 														Dodaj( Zmienna("i"), Stala(1) )
	 													), 
	 									InstrukcjaAssign( 
	 														Zmienna("sum"), 
	 														Dodaj( Zmienna("sum"), Zmienna("i") ) 
	 													)
	 								) 
	 					)
	 )


print( 
	 	ZlozInstrukcje( 	InstrukcjaAssign( Zmienna("sum"), Stala(0) ), 
	 						forLoop( 	InstrukcjaAssign( Zmienna("i"), Stala(0) ), 
	 									LessEqualThan( Zmienna("i"), Stala(10) ), 
	 									InstrukcjaAssign( 	Zmienna("i"), 
	 														Dodaj( Zmienna("i"), Stala(1) )
	 													), 
	 									InstrukcjaAssign( 
	 														Zmienna("sum"), 
	 														Dodaj( Zmienna("sum"), Zmienna("i") ) 
	 													)
	 								) 
	 					).wykonaj( dict() )
	 )
