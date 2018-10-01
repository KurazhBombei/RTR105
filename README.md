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


