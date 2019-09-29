Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request as ur
>>> 
>>> while True:
	area = input("Area:")
	con = ur.urlopen("http://127.0.0.1:8000/ml/api/simple-linear-regression/?area=%s"%(area))
	print(con.read.decode())

	
Area:100
Traceback (most recent call last):
  File "<pyshell#6>", line 4, in <module>
    print(con.read.decode())
AttributeError: 'function' object has no attribute 'decode'
>>> 
>>> 
>>> while True:
	area = input("Area:")
	con = ur.urlopen("http://127.0.0.1:8000/ml/api/simple-linear-regression/?area=%s"%(area))
	print(con.read().decode())

	
Area:100
Predicted value: <h1>predicted value: [865.8914728682166]</h1>
Area:100,200,1000
Predicted value: <h1>predicted value: [865.8914728682166, 1949.6124031007748, 10619.37984496124]</h1>
Area:
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    area = input("Area:")
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> def prediction(x):
	return *x
SyntaxError: invalid syntax
>>> def prediction(x):
	con = ur.urlopen("http://127.0.0.1:8000/ml/api/simple-linear-regression/?area=%s"%(",".join(x)))
	print(con.read().decode())

	
>>> 
>>> prediction([100,1000])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    prediction([100,1000])
  File "<pyshell#17>", line 2, in prediction
    con = ur.urlopen("http://127.0.0.1:8000/ml/api/simple-linear-regression/?area=%s"%(",".join(x)))
TypeError: sequence item 0: expected str instance, int found
>>> 
>>> 
>>> def prediction(x):
	con = ur.urlopen("http://127.0.0.1:8000/ml/api/simple-linear-regression/?area=%s"%(",".join(map(lambda n: str(n),x))))
	print(con.read().decode())

	
>>> 
>>> 
>>> prediction([100,1000])
Predicted value: <h1>predicted value: [865.8914728682166, 10619.37984496124]</h1>
>>> 
>>> 
>>> 
>>> 
