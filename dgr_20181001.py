Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.__doc

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    __builtins__.__doc
AttributeError: 'module' object has no attribute '__doc'
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> a = 20
>>> a
20
>>> b = 1.56
>>> b
1.56
>>> b*b
2.4336
>>> c = 'A'
>>> vars()
{'a': 20, 'c': 'A', 'b': 1.56, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'str'>
>>> A

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    A
NameError: name 'A' is not defined
>>> TYPE(b)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    TYPE(b)
NameError: name 'TYPE' is not defined
>>> 
