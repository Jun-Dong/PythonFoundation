Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> set1 = set([1,2,3,3,4,5,4])
>>> set1
{1, 2, 3, 4, 5}
>>> set1.add(6)
>>> ser1
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ser1
NameError: name 'ser1' is not defined
>>> set1
{1, 2, 3, 4, 5, 6}
>>> num3 = frozenset([1,2,3,4,5,5])
>>> num3
frozenset({1, 2, 3, 4, 5})
>>> num3.add(6)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num3.add(6)
AttributeError: 'frozenset' object has no attribute 'add'
>>> type(num3)
<class 'frozenset'>
>>> type(set1)
<class 'set'>
>>> 
