import sys
import os

def register():
    print("Register")
    username=input("Enter Username:-")
    password=int(input("Enter Password:-"))
    email=input("Enter Email:-")  
    phone_no=int(input("Enter Phone No:-"))
    age=int(input("Enter Age:-"))

    print("\n-----Registration Successful-----")
    login(username,password,email,phone_no,age)

def login(username,password,email,phone_no,age):
    print("\n----Login Your Account-------")
    user=input("Enter Username:-")
    passw=int(input("Enter Password:-"))
    if user==username and passw==password:
        print("Login Successful\n\n")
        print("-----Let's go in booking system------\n\n")
        booking(username,password,email,phone_no,age)

    else:
        print("Login Failed")
        print("Please Try Again")
        login(username,password,email,phone_no,age)

def booking(username,password,email,phone_no,age):
    print("!-------Welcome to Booking System--------!\n\n")
    print("Select From Below:-\n")
    print("1.Book a Ticket")
    print("2.Cancel a Ticket")
    print("3.Exit")
    choices=int(input("Enter your choice :-\n\n"))
    match choices:
        case 1:
          source=input("Enter Source:-")
          destination=input("Enter Destination:-")
          print("\n\n!-----Available bus are-------!\n\n1.Shivshai\n2.Shivaji Travels\n3.ST Mahamandal\n4.Shivneri\n")
          choicebus=int(input("Select bus from which you are going to travel:-"))
          if choicebus==1:
            shivshai(username,password,email,phone_no,age,source,destination)
          elif choicebus==2:
            shivaji(username,password,email,phone_no,age,source,destination)
          elif choicebus==3:  
            stmahamandal(username,password,email,phone_no,age,source,destination)
          elif choicebus==4:
            shivneri(username,password,email,phone_no,age,source,destination)
          else:
            print("Invalid Choice")
            booking()
        case 2:  
          cancel()
        case 3:
          exit()
        case _:
          print("Invalid Choice")
          booking()

def cancel():
  print("Your booking has been cancelled")
  sys.exit()
def exit():
  print("Thank You")
  sys.exit()

def shivshai(username,password,email,phone_no,age,source,destination):
  print("\n\n!----You have selected Shivshai bus---!\n\n")
  seats=input("how many ticket you have to book:-")
  choiceseat=int(input("choice of seats are:-\n1.Window seat\n2.Middle seat\n3.last seats\n"))
  if choiceseat==1:
    print("\nYou have selected window seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"Destination:-",destination)
      print("\nYou have booked",seats,"ticket at Window seat")
    else:
      print("Thank you for visiting")
  elif choiceseat==2:
    print("\nYou have selected middle seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"Destination:-",destination)
      print("\nYou have booked",seats,"ticket at Middle seat")
    else:
        print("Thank you for visiting")
  elif choiceseat==3:  
    print("\nYou have selected last seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"Destination:-",destination)
      print("\nYou have booked",seats,"ticket at last seat")
    else:
        print("Thank you for visiting")
  else :
    print("Invalid Choice")




def shivaji(username,password,email,phone_no,age,source,destination):

print("\n\n!-----You have selected Shivsaji Travel bus------!\n\n")
  seats=input("how many ticket you have to book:-")
  choiceseat=int(input("choice of seats are:-\n1.Window seat\n2.Middle seat\n3.last seats\n"))
  if choiceseat==1:
    print("\nYou have selected window seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination:-",destination)
      print("\nYou have booked",seats,"ticket at Window seat")
    else:
        print("Thank you for visiting")
  elif choiceseat==2:
    print("\nYou have selected middle seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination:-",destination)
      print("\nYou have booked",seats,"ticket at Middle seat")
    else:
        print("Thank you for visiting")
  elif choiceseat==3:  
    print("\nYou have selected last seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination:-",destination)
      print("\nYou have booked",seats,"ticket at Last seat")
    else:
        print("Thank you for visiting")
  else :
    print("Invalid Choice")




def stmahamandal(username,password,email,phone_no,age,source,destination):
  print("\n\n!-------You have selected ST Mahamadal bus------!")
  seats=input("how many ticket you have to book:-")
  choiceseat=int(input("choice of seats are:-\n1.Window seat\n2.Middle seat\n3.last seats\n\n"))
  if choiceseat==1:
    print("\nYou have selected window seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination",destination)
      print("\nYou have booked",seats,"ticket at Window seat")
    else:
        print("Thank you for visiting")
  elif choiceseat==2:
    print("\nYou have selected middle seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination",destination)
      print("\nYou have booked",seats,"ticket at Middle seat")
    else:
        print("Thank you for visiting")
  elif choiceseat==3:  
    print("\nYou have selected last seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination",destination)
      print("\nYou have booked",seats,"ticket at Last seat")
    else:
        print("Thank you for visiting")
  else :
    print("Invalid Choice")





def shivneri(username,password,email,phone_no,age,source,destination):
  print("\n\n!-------You have selected Shivneri bus------!")
  seats=input("how many ticket you have to book:-")
  choiceseat=int(input("choice of seats are:-\n1.Window seat\n2.Middle seat\n3.last seats\n\n"))
  if choiceseat==1:
    print("\nYou have selected window seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
       print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination",destination)
       print("\nYou have booked",seats,"ticket at Window seat")
    else:
        print("Thank you for visiting")

elif choiceseat==2:
    print("\nYou have selected middle seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination",destination)

      print("\nYou have booked",seats,"ticket at Middle seat")
    else:
        print("Thank you for visiting")
  elif choiceseat==3:  
    print("\nYou have selected last seat")
    confirm=input("Do you want to confirm your booking:- yes or no:-")
    if confirm=="yes":
      print("\nUsername:-",username ,"\nEmail:-",email,"\nPhone number:-",phone_no,"\nAge:-",age,"\nSource:-",source,"\nDestination",destination)
      print("\nYou have booked",seats,"ticket at last seat")
    else:
        print("Thank you for visiting")
  else :
    print("Invalid Choice")




  def confirm(seats,choiceseat):
    if confirm==1 and choiceseat==1:
      print("\nYou have bookeed",seats,"ticket at Window seat")
    else:
      print("Thank you for visiting our website")
      sys.exit()

print("-------------------------")
print("Online bus booking system")
print("-------------------------\n")
choice=int(input("Choose \n1.Register \n2.Login \n3.exit\n"))
match choice:
 case 1:
   register()
 case 2:
   login(username,password,email,phone_no,age)
 case 3:
  print("Thank you for using our service")
 case _:
  print("invalid choice"
