try:
    rawstr = input("Enter a number:")
    ival = int(rawstr)
except:
    ival =  'R'

if ival == "R":
    print("not a number")
else:
    print("Good job")
