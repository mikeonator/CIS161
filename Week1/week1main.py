#Michael Audi - CSC161 Week 1 Main Assignment

##Dependencies
import datetime
import calendar


##Problem 1

##Setting Pet name and type, then printing that info using an f string
pet_type = "fish"
pet_name = "Val"
print(f"\nI used to have a {pet_type} and her name was {pet_name}.")


##Problem 2

###Acquiring User data for further manipulation using input and saving each as a variable
first_name = str(input("\nEnter your first name.\n"))
current_age = int(input("\nEnter your current age.\n"))
yearly_save = int(input("\nEnter your yearly savings.\n"))

###Printing the above data using f-strings and modifiers
print(f"\nHello {first_name}! You are currently {current_age} years old.")
print(f"In 10 years, you will be {10 + current_age} years old!")
print(f"If you save ${yearly_save} each year, in 5 years you'll have saved ${5*yearly_save}!")
print(f"Your average monthly savings are ${(yearly_save/12):.2f}")


##Problem 3

###Defining the number of seconds in a day.
seconds_day = 86400

###Acquring current date and time, saving the current year and month, as well as the full name of the current month.
now = datetime.datetime.now()
current_year = now.year
current_month = now.month
current_month_name = now.strftime("%B")

###using monthrange to acquire the number of days in the current month ([1] because the second value the function outputs is what we need)
days_current_month = calendar.monthrange(current_year, current_month)[1]

###Printing the number of seconds in a day multiplied by the number of days in the month along with the full name of the month.
print(f"\nThere are {seconds_day * days_current_month} seconds in the current month of {current_month_name}.")


##Problem 4

###Take user input on total number of eggs
number_eggs = int(input("\nEnter the number of eggs you have.\n"))

###Print Egg dozen values using printf modifiers and operators
print(f"\nYou have {(number_eggs//12):.0f} full dozens of eggs, and {(number_eggs%12):.0f} eggs remaining\n")