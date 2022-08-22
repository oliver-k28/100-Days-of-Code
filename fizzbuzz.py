#FizzBuzz
#program should print each number from 1 to 100 in turn.
#when the number is divisible by 3 then instead of printing the number it should print "Fizz".
#when the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#and if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)