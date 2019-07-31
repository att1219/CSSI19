num= raw_input("Enter a number")
num=int(num) #converts variable into an integer

if type(num) <> type(int()):
    print "Not an integer"
elif num<1 and num>10:
    print "out of range"
elif num%2==0:
    if num==2:
        print "That's a prime number!"
    else:
        print "That's not a prime number."
else : 
    if num == 3 or num == 5 or num == 7:
        print "That's a prime number!"
    else:
        print "That's not a prime number."