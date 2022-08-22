#this program tells you how many weeks of life you have left

age = input("What is your current age? ")

#assume living to 90
age = (90 - int(age))

days = age * 365
weeks = age * 52
months =  age * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left." )