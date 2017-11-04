Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def Fun1():
	x = 5
	def Fun2():
		x *= x
		return x
	return Fun2()

>>> Fun1()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Fun1()
  File "<pyshell#4>", line 6, in Fun1
    return Fun2()
  File "<pyshell#4>", line 4, in Fun2
    x *= x
UnboundLocalError: local variable 'x' referenced before assignment
>>> def Fun1():
	x = [5]
	def Fun2():
		x[0] *= x[0]
		return x[0]
	return Fun2()

>>> Fun1()
25
>>> def Fun1():
	x = 5
	def Fun2():
		nonlocal x
		x *= x
		return x
	return Fun2()

>>> Fun1()
25
>>> 
