# RTR105
Datormacibus kursa elektroniska klade

2.nodarbiba




Ctrl.+Alt.+T = open command line.
letter+TABx2 = show commands list starting with current character.
Ctrl.+L = clean console.
man command = command description (manual).
command -key(a,b,t etc.)
echo $0 = ...
Ctrl.+Alt.+Fx = open alternative command line.
pwn = file sistem.
ls = list of files : key -l = show long list of files and print author of each file : key -a = show hiden files starting with .
ls -file = show concrete file.
ls -d = directories list.
who = show current user.
whoami = print user ID.
Ctrl.+Shift+T = create new tab in command line.





3.nodarbiba





cd = wondering throughfile sistem
. = current directory
.. = back
/ = root
cd can be used with fool adress
~ = home (cd ~)
cd+Enter = bring you to home
mkdir = make directory
rmdir = remove directory (do not remove if there is something inside, except case of special key using)
rm = remove (-r = easy key to remove folder with content)
echo "Tekst" = show text in console(direct screen)
echo -e = key for take into account commands like \n
\n = used to remove text on to next line(echo -e "Text\nText"
cat; more; less = used to read fail content (cat fails1.txt)
echo "Text" > fails1.txt = create fail with "Text" content
echo "Add. Text" >> fails1.txt = will add "Add. Text" on second line, in file fails1.txt
nano = fail redactor
rwx rwx rwx = permitions
101 100 000 = convert to dec systema.
 5   4   0
 chmod = change permitions (chmod 540)
 cp = copy (copy fails1.txt fails101.txt)
 mv = move
 *1*.txt = argument (will move all txt files with "1" in file name) (mv *1*.txt repo./)
 mv fails1.txt fails3.txt = rename or rewrite if alreedy exist fails3.txt
 mv fails1.txt repo./fails2.txt = move and rename
 
 
 
 
 
 
4.nodarbiba





nano nosaukums.sh - create script

Script contain.
#!/bin/bash <- set interpritator
mkdir Mape
cd Mape
mkdir MapeMape
 
/home/user/nosaukums.sh - do script
echo $PATH - pathes list
PATH=$PATH:directory - add new directory to pathes list
if new path(/home/user/) added can be used just name (nosaukums.sh)
clone https//:github.come/user_name/directory - clone directory from github





5.nodarbiba





vars() - function which show items list
__builtins__ - object
__doc__ - method (__builtins__.doc__ - show documentation about builtins)
print() - function for reflection information on display
= - assigments operation (a = 20; b = 1.56 ; c = 'A' ('- need to insert A like a character) 
type() - function for reflection data type (type(a))
'int' - data type of whole numbers
'float' - data type of real numbers
'str' - data typpe for character lines





6.nodarbiba




constants - nummers and characters( 5; 5.5 ; ABC )
print() - display argument entered in parentheses

A variable is a named place in the memory where a programmer can store
data and later retrieve the data using the variable “name” (x=5 - set x value as 5)

Variables have to:
start with a letter or underscore _
consist of letters, numbers, and underscores
Good: spam eggs spam23 _speed
Bad: 23spam #sign var.12
Different: spam Spam SPAM

x = 2
x = x + 2
print(x) -> 4

+ Addition
- Subtraction
* Multiplication
/ Division
** Power
% Remainder

Highest precedence rule to lowest precedence rule:
• Parentheses are always respected
• Exponentiation (raise to a power)
• Multiplication, Division, and Remainder
• Addition and Subtraction
• Left to right
x = 1 + 2 ** 3 / 4 * 5
>>> print(x)
11.0

type() - show variable format(string, integer, float)
input() - request argument from user
Python ignore text after -> #





7.nodarbiba.




x = 5
if x > 1:
     print(X)
Output: 5
quantity of spaces determine level on which you enter instructions.

Python Meaning
<      Less than
<=     Less than or Equal to
==     Equal to
>=     Greater than or Equal to
>      Greater than
!=     Not equal

Nested decision: 
x = 42
if x > 1 :
    print('More than one')
    if x < 100 :
         print('Less than 100')
print('All done')

Two-way decision:
x = 4
if x > 2 :
     print('Bigger')
else :
     print('Smaller')
print('All done')

else: -> choose all lefted cases, except if cases.

Multi-way:
x = 0
if x < 2 :
     print('small')
elif x < 10 :
       print('Medium')
else :
     print('LARGE')
print('All done')

If the code in the try works - the except is skipped
If the code in the try fails - it jumps to the except section

astr = 'Hello Bob'
try:
 istr = int(astr)
except:
 istr =-1
print('First', istr)
astr = '123'
try:
 istr = int(astr)
except:
 istr =-1
print('Second', istr)

Output: First-1; Second 123

rawstr = input('Enter a number:')
try:
 ival = int(rawstr)
except:
 ival = -1
if ival > 0 :
 print('Nice work')
else:
 print('Not a number')
 
 
 
 
 8. nodarbiba
 
 
 
 
 
 def -> used to determine function(def things():)
 
 def thing():
   print('Hello')
   print('Fun')
things()
output: Hello 
        Fun
        
In Python a function is some reusable code that takes
arguments(s) as input, does some computation, and then returns
a result or results

big = max('Hello world')
>>> print(big)
w
>>> tiny = min('Hello world')
>>> print(tiny)

>>>

>>> def greet(lang):
... if lang == 'es':
... print('Hola')
... elif lang == 'fr':
... print('Bonjour')
... else:
... print('Hello')
...
>>> greet('en')
Hello
>>> greet('es')
Hola
>>> greet('fr')
Bonjour
>>>


def greet():
 return "Hello"
print(greet(), "Glenn")
print(greet(), "Sally")
output: Hello Glenn
        Hello Sally
        
        
Multiple Parameters / Arguments:        

def addtwo(a, b):
 added = a + b
 return added

When a function does not return a value, we call it a “void”
function
Functions that return values are “fruitful” functions
Void functions are “not fruitful”



9.nodarbiba



Loop:
n = 5
while n > 0 :
 print(n)
 n = n – 1
print('Blastoff!')
print(n)
 
 # while function while argument is performed it will redo function body.
 
 Infinit loop:
 n = 5
while n > 0 :
 print('Lather')
 print('Rinse')
print('Dry off!')

Another inf.loop:
n = 0
while n > 0 :
 print('Lather')
 print('Rinse')
print('Dry off!')

while True:
 line = input('> ')
 if line == 'done' :
 break
 print(line)
print('Done!')
#break is is used break loop.


#The continue statement ends the current iteration and jumps to the
top of the loop and starts the next iteration.
while True:
 line = input('> ')
 if line[0] == '#' :
 continue
 if line == 'done' :
 break
 print(line)
print('Done!')


Indefinite Loops:
While loops are called “indefinite loops” because they keep
going until a logical condition becomes False

Definite Loops:
• Quite often we have a list of items of the lines in a file -
effectively a finite set of things
• We can write a loop to run the loop once for each of the items in
a set using the Python for construct
• These loops are called “definite loops” because they execute an
exact number of times
• We say that “definite loops iterate through the members of a set”

Example:
for i in [5, 4, 3, 2, 1] :
      print(i)                       Output: 1 2 3 4 5
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
          print('Happy New Year:', friend)
print('Done!')
Output: Happy New Year: Joseph
        Happy New Year: Glenn
        Happy New Year: Sally
        Done!
        
Finding the Largest Value:
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
           if the_num > largest_so_far :
                    largest_so_far = the_num
           print(largest_so_far, the_num)
print('After', largest_so_far)

Counting in a Loop:
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
 zork = zork + 1
 print(zork, thing)
print('After', zork)


Summing in a Loop:
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
     zork = zork + thing
     print(zork, thing)
print('After', zork)
Output:
Before 0
9 9
50 41
62 12
65 3
139 74
154 15
After 154


Finding the Average in a Loop:
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
 count = count + 1
 sum = sum + value
 print(count, sum, value)
print('After', count, sum, sum / count)

Filtering in a Loop:
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
        if value > 20:
             print('Large number',value)
print('After')

Search Using a Boolean Variable:
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
     if value == 3 :
         found = True
     print(found, value)
print('After', found)

How to Find the Smallest Value:
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
     if the_num > largest_so_far :
             largest_so_far = the_num
     print(largest_so_far, the_num)
print('After', largest_so_far)
Output:
Before -1
9 9
41 41
41 12
41 3
74 74
74 15
After 74


Finding the Smallest Value:
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
 if smallest is None :
 smallest = value
 elif value < smallest :
 smallest = value
 print(smallest, value)
print('After', smallest)
Output:
Before
9 9
9 41
9 12
3 3
3 74
3 15
After 3


is equal to ==
is not equal to !=


