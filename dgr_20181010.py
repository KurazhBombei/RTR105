Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(123)
123
>>> print(98.6)
98.6
>>> print("Hello world")
Hello world
>>> x = 12.2
>>> y = 14
>>> x = 100
>>> x
100
>>> y
14
>>> x1q3z9ocd = 35
>>> x1q3z9afd = 12.50
>>> x1q3p9afd = x1q3z9ocd * x1q3z9afd
>>> 
KeyboardInterrupt
>>> x1q3p9afd
437.5
>>> print(x1q3p9afd)
437.5
>>> x1q3z9ocd = 35
>>> x = 2
>>> x = x + 2
>>> x
4
>>> x
4
>>> y
14
>>> c = x**y
>>> c
268435456
>>> f=999
>>> g=1000
>>> h=f%g
>>> h
999
>>> h=f+g
>>> h
1999
>>> h=f/g
>>> h
0
>>> h=f%g
>>> h
999
>>> a=2
>>> b=2
>>> c=a**b
>>> c
4
>>> x=1+2**3/4*5
>>> x
11
>>> eee="hello"+"there"
>>> eee
'hellothere'
>>> eee="hello" + "there"
>>> eee
'hellothere'
>>> eee="hello" +""+ "there"
>>> eee
'hellothere'
>>> eee="hello" +" "+ "there"
>>> eee
'hello there'
>>> eee=eee+1

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    eee=eee+1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type("hello")
<type 'str'>
>>> type(1)
<type 'int'>
>>> type(1)
<type 'int'>
>>> type(h)
<type 'int'>
>>> type(1.5)
<type 'float'>
>>> i=42
>>> type(1)
<type 'int'>
>>> f=float(i)
>>> f
42.0
>>> type(f)
<type 'float'>
>>> sval="123"
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> print(ival+1)
124
>>> type(ival)
<type 'int'>
>>> nsv="hello bob"
>>> niv=int(nsv)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    niv=int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nam=input("who are you?")
who are you? Tim

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    nam=input("who are you?")
  File "<string>", line 1, in <module>
NameError: name 'Tim' is not defined
>>> nam = input("who are you?")
who are you?

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    nam = input("who are you?")
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> nam = input("who are you?")
who are you? print("welcom", nam)

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    nam = input("who are you?")
  File "<string>", line 1
    print("welcom", nam)
        ^
SyntaxError: invalid syntax
>>> nam = input("who are you?")
who are you? TIm

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    nam = input("who are you?")
  File "<string>", line 1, in <module>
NameError: name 'TIm' is not defined
>>> nam = input("who are you?")
who are you? Chuck

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    nam = input("who are you?")
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> nam = raw_input("who are you?")
who are you? Tim
>>> print("Welcome", nam)
('Welcome', ' Tim')
>>> print('Welcome', nam)
('Welcome', ' Tim')
>>> inp = input('Europe floor')
Europe floor 0
>>> usf = int(inp) + 1
>>> usf
1
>>> print('US floor', usf)
('US floor', 1)
>>> #Get the name of the file and open it
>>> name=input('Enter file:')
Enter file: lololo

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    name=input('Enter file:')
  File "<string>", line 1, in <module>
NameError: name 'lololo' is not defined
>>> name=input('Enter file:')
Enter file:git-upload

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    name=input('Enter file:')
  File "<string>", line 1, in <module>
NameError: name 'git' is not defined
>>> name=raw_input('Enter file:')
Enter file:git-upload
>>> name
'git-upload'
>>> handle=open(name, 'r')
>>> handle
<open file 'git-upload', mode 'r' at 0x7fb4e1afa8a0>
>>> for line in handle:
	print(line)

	
#!/bin/bash

if [ $# == 1 ]

then

git config --global user.email InspektorTimchik@gmail.com

git add .

#git commit -m "20180926_13_50"

git commit -m $1

git push origin master

fi

>>> name=raw_input('Enter file:')
Enter file:lololo
>>> handle=open(name, 'r')

Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    handle=open(name, 'r')
IOError: [Errno 2] No such file or directory: 'lololo'
>>> for line in handle:
	print(line)

	
>>> 
