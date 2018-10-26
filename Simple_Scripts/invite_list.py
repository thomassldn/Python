#Author: Thomas S
#Date: 26 Oct 18
#Desc:Small program that sends a mass messeage to a group of people in a list

#start of program
email_recipients = ['Alex', 'John', "Anthony", "Jose"]

for x in email_recipients:

 print("Hello " + x + ",\n" + "You are invited ..\n") 


#OUTPUT: 
#$ python invite_list.py
#Hello Alex,
#You are invited ..

#Hello John,
#You are invited ..

#Hello Anthony,
#You are invited ..

#Hello Jose,
#You are invited ..

#end of program 
