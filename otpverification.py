import os
import math
import random
import smtplib

digits="0123456789"
OTP=""  
#create a 6-digit random number
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
#store the number in a variable
otp = OTP + " is your OTP"

#program to send emails
#we need to use OTP as a message
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
#request two user inputs; first for the user’s email and then for the OTP that the user has received
s.login("Your Gmail Account", "You app password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")      
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")