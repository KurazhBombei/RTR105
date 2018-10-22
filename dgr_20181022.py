Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: /home/user/RTR105/2scr13.py ====================
Hello
Fun
Zip
Hello
Fun
>>> 
==================== RESTART: /home/user/RTR105/2scr14.py ====================
w
>>> 
==================== RESTART: /home/user/RTR105/2scr14.py ====================
w
 
>>> 
==================== RESTART: /home/user/RTR105/2scr14.py ====================
c
a
>>> print(max.__doc__)
max(iterable[, key=func]) -> value
max(a, b, c, ...[, key=func]) -> value

With a single iterable argument, return its largest item.
With two or more arguments, return the largest argument.
>>> 
==================== RESTART: /home/user/RTR105/2scr14.py ====================
a
a
>>> 
==================== RESTART: /home/user/RTR105/2scr15.py ====================
>>> 
==================== RESTART: /home/user/RTR105/2scr15.py ====================
>>> 
==================== RESTART: /home/user/RTR105/2scr15.py ====================
0.99
>>> 
==================== RESTART: /home/user/RTR105/2scr15.py ====================
0.99
42.0
-2.5
>>> 
==================== RESTART: /home/user/RTR105/2scr15.py ====================
0.99
42.0
-2.5
>>> print(f)
42.0
>>> print(i)
42
>>> type(f)
<type 'float'>
>>> type(i)
<type 'int'>
>>> sval = "123"
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nsv = "hello bob"
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and i work all day.')
print_lyrics
SyntaxError: invalid syntax
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and i work all day.')
print_lyrics
SyntaxError: invalid syntax
>>> 
==================== RESTART: /home/user/RTR105/2scr16.py ====================
>>> print_lyrics
<function print_lyrics at 0x7fbaeb3946e0>
>>> 
==================== RESTART: /home/user/RTR105/2scr16.py ====================
Hello
Yo
7
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and i work all day.
>>> 
==================== RESTART: /home/user/RTR105/2scr17.py ====================
hello
Hola
Bonjour
>>> return "YOLO"
SyntaxError: 'return' outside function
>>> 
==================== RESTART: /home/user/RTR105/2scr18.py ====================
('Hello', 'Glen')
('Hello', 'Sally')
>>> 
==================== RESTART: /home/user/RTR105/2scr19.py ====================
('Hello', 'Glenn')
('Hola', 'Sally')
('Bonjour', 'Michael')
>>> 
==================== RESTART: /home/user/RTR105/2scr20.py ====================
8
>>> history

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    history
NameError: name 'history' is not defined
>>> hystory

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    hystory
NameError: name 'hystory' is not defined
>>> history > history_20181022.txt

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    history > history_20181022.txt
NameError: name 'history' is not defined
>>> 
