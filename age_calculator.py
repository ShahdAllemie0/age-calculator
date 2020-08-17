from datetime import datetime
from datetime import date
def check_birthdate(year, month, day):
  
	     # write code here
       
          birthdate = date(int(year), int(month),int(day) )
          today = date.today()
          if birthdate<today:
           return True
          else:
           return False

def calculate_age(year, month, day):
          birthdate = date(int(year), int(month),int(day) )
          today = date.today()
          age=today - birthdate
          agedays=age.days
          yourage=int(agedays/365)
          print("You are %d years old."%(yourage)) 

def main():
	# write main code here
	    
   year=input("Enter year of birth: ")
   month=input("Enter month of birth: ")
   day=input("Enter day of birth: ")

 
   if(check_birthdate(year,month,day))==True:
     calculate_age(int(year), int(month),int(day))
   else:
     print("the birthdate is invalid" )


if __name__ == '__main__':
	main()



