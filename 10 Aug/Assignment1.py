#1) Reverse a String and print it on console "Python Skills" .
print("---Answer 1---")
txt = "Python Skills"[::-1]
print(txt)

#2) Assign String to x variable in DD-MM-YYYY format extract and print Year from String.
print("---Answer 2---")
import datetime
x = "19-08-2021" 
print("Year:",x[6:])

#3)In a small company, the average salary of three employees is Rs1000 per week. If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn? Solve by using Python programm
print("---Answer 3---")
e1=1100
e2=500
e3=0
avg=1000
totalsalaryof3emp=1000*3
e3=totalsalaryof3emp-e1-e2
print("Salary of third employee is Rs.",e3)

#4) Write Program - convert a percentage to a fraction (To convert a percentage into fraction let say 30% to a fraction)
print("---Answer 4---")
percent=30
f=percent/100
n=percent
d=100
#simplyfing the fractions
num=n/10
den=d/10
print("Fraction is" ,int(num),"/",int(den))


#5)Write Program - A train 340 m long is running at a speed of 45 km/hr. what time will it take to cross a 160 m long  tunnel?
print("---Answer 5---")
lengthoftrain=340
lengthoftunnel=160
#Total distance to be travelled by train
distance=lengthoftrain+lengthoftunnel
#conversion of km per hour into min per seconds
speed=45*5/18
time=distance/speed
print("Time taken by train to cross the tunnel=",time,"secs")