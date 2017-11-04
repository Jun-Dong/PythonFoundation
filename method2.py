Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def SaySome(names,words)
SyntaxError: invalid syntax
>>> def SaySome(name,words):
	print(name + "->" + words)

	
>>> SaySome("小甲鱼",'哈哈哈')
小甲鱼->哈哈哈
>>> SaySome(words='哈哈哈',name='小技术')
小技术->哈哈哈
>>> def SaySome(name='小甲鱼',words=)
SyntaxError: invalid syntax
>>> def SaySome(names='小甲鱼',words='晋级赛'):
	'文档'
	#注释
	print(name+'->'+words)

	
>>> SaySome()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    SaySome()
  File "<pyshell#11>", line 4, in SaySome
    print(name+'->'+words)
NameError: name 'name' is not defined
>>> def SaySome(name='小甲鱼',words='晋级赛'):
	'文档'
	#注释
	print(name+'->'+words)

	
>>> SaySome()
小甲鱼->晋级赛
>>> SaySome._doc_
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    SaySome._doc_
AttributeError: 'function' object has no attribute '_doc_'
>>> SaySome.__doc__
'文档'
>>> print(len("年后"));
2
>>> def test(*params):
	print("参数的长度是:",len(params));
	print("第二个参数的长度是",len(params));

	
>>> def test(*params):
	#"可变参数"
	print("参数的长度是:",len(params));
	print("第二个参数的长度是",len(params));

	
>>> test(1,"小甲鱼",22211,222.11,22)
参数的长度是: 5
第二个参数的长度是 5
>>> def test(*params):
	#"可变参数" 元组
	print("参数的长度是:",len(params));
	print("第二个参数是",params[1]);
	print("第二个参数的长度是",len(params));
