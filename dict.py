Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dictl = {'吃了没有':'吃了','耐克':'Just do it'}
>>> print('耐克口号:'dictl['耐克'])
SyntaxError: invalid syntax
>>> print('耐克口号:',dictl['耐克'])
耐克口号: Just do it
>>> dictl
{'吃了没有': '吃了', '耐克': 'Just do it'}
>>> dictl['爱迪生'] = "99%天才1%灵感"
>>> dictl
{'吃了没有': '吃了', '耐克': 'Just do it', '爱迪生': '99%天才1%灵感'}
>>> 
