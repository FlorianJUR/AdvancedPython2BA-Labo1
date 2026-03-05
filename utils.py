import math
from scipy import integrate as sp_integrate

def fact(n): 

	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""

	try:
		return math.factorial(n)
	except ValueError:
		print("Entrez un nombre > 0 dans la fonction fact ")


def roots(a, b, c):

	"""Computes the roots of the ax^2 + bx + c = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""

	delta = b*b-(4*a*c)
	if delta < 0:
		return ()
	elif delta == 0:
		return (-b/(2*a))
	elif a==0:
		return (-c/b)
	else:
		root1 = (-b+math.sqrt(delta))/(2*a)
		root2 = (-b-math.sqrt(delta))/(2*a)
		return (root1, root2)


def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower' and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
		
def integrate(function, lower, upper):
    def f(x):
        return eval(function, {"x": x, "math": math})
    
    result, _ = sp_integrate.quad(f, lower, upper)
    return result

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
