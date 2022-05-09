# HEAVEN BARNES
# Hello there player it's time to play Age Calculation
#import date form datetime
 
from datetime import date 
y = date.today().year

m = date.today().month

d = date.today().day 

# Create input message asking user to enter his or hers birth date.
print(date.today())

year = int(input("Enter your birth year... "))

month = int(input("Enter your birth month... "))

day = int(input("Enter your birth day... "))

if day > d and month >= m:
    dd = (d + 30) - day
    mm = ((m - 1) + 12) - month
    yy = (y - 1) - year
    print(" Hello my name is Heaven " + str(yy) +  " Years " +  (str(mm) +  " Months " +  str(dd) +  " Days "))

elif day > d and month < m:
    dd = (d + 30) - day
    mm = m - month
    yy = y - year
    print(str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days ")
elif day < d and month > m:
    dd = d - day
    mm = (m + 12) - month
    yy = (y - 1) - year
    print(str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days ")
else:
    dd = d - day
    mm = m - month
    yy = y - year
    print(str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days ")
    