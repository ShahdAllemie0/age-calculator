# from datetime import datetime

# def check_birthdate(year, month, day):
# 	# write code here

# def calculate_age(year, month, day):
#     # write code here

# def main():
# 	# write main code here


# if __name__ == '__main__':
# 	main()
def main():
    
   year=input("Enter year of birth:")
   month=input("Enter month of birth:")
   day=input("Enter day of birth:")
   from datetime import date  
   def check_birthdate(year,month,day):
      birthdate = date(int(year), int(month),int(day) )
      today = date.today()
      if birthdate<today:
        calculate_age(int(year), int(month),int(day))
        return True
      else:
        print("the birthdate is invalid" )
        return False
        
        # return "the birthdate is invalid"  
   def calculate_age(year,month,day):
          birthdate = date(int(year), int(month),int(day) )
          today = date.today()
          age=today - birthdate
          agedays=age.days
          yourage=int(agedays/365)
          print("You are %d years old."%(yourage))  
   check_birthdate(year,month,day)   

if __name__ == '__main__':
	main()
