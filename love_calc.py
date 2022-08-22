#program that tests the compatibility between two people.
#take both people's names and check for the number of times the letters in the word TRUE occurs. 
#then check for the number of times the letters in the word LOVE occurs. 
#then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = (name1.lower() + name2.lower())

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

true = str(t+r+u+e)

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

love = str(l+o+v+e)

love_score = int(true + love)


if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50: 
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your  score is {love_score}.")
