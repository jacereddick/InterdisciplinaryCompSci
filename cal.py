import sys
import stdio
import math




# Accepting two different integers from the command line for the month and year
#desired for the calendar
   
mm = int(sys.argv[1])
yy = int(sys.argv[2])

#A dictionary in order to be able to index a value with a month that could
#be inputted
month ={1:'January', 2:'February', 3:'March', 
        4:'April', 5:'May', 6:'June', 7:'July',
        8:'August', 9:'September', 10:'October',
        11:'November', 12:'December'}
   
# code below for calculation of odd days (in order to find the 1st day of the
#month
day =(yy-1)% 400
day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
day = day % 7

#Setting up the lists/arrays for days per month for each kind of year, whether
#that be a leap year or no leap year
nly =[31, 28, 31, 30, 31, 30, 
      31, 31, 30, 31, 30, 31]
ly =[31, 29, 31, 30, 31, 30, 
     31, 31, 30, 31, 30, 31]
s = 0


#Deciphering the leap years through calculations of every 4 years
if yy % 4 == 0:
    for i in range(mm-1):
        s+= ly[i]
else:
    for i in range(mm-1):
        s+= nly[i]

#Setting the day during the week by dividing by 7
day += s % 7
day = day % 7
   
# Used for spacing between the days on the calendar
space =''
space = space.rjust(2, ' ')
  
# Printing the calendar and calculating to see if the year is a leap year, then
#deciphering from that what the monthly calendar for the indicated month that
#year looks like
stdio.write(str(month[mm]) + str(yy))
stdio.writeln()
stdio.writeln('Su '+ 'Mo '+ 'Tu '+ 'We '+ 'Th '+ 'Fr '+ 'Sa ')
  
if mm == 9 or mm == 4 or mm == 6 or mm == 11: 
    for i in range(31 + day):
          
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()
                
#If the month is February (Potential Leap Year)
elif mm == 2:
    if yy % 4 == 0:
        p = 30
    else:
        p = 29
          
    for i in range(p + day):
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()
#If the mm value is not 2 (not February)
else:
    for i in range(32 + day):
          
        if i<= day:
            print(space, end =' ')  
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()
stdio.writeln()
