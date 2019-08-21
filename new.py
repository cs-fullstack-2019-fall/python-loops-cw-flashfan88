# Exercise 1:
# Print -20 to and including 50. Use any loop you want.

# for num in range(-20, 50 + 1, 1):
#      print(num)

# Exercise 2:
# Create a loop that prints even numbers from 0 to and including 20.
# Hint: You can find multiples of 2 with (whatever_number % 2 == 0)

# for whatevernumber in range(0, 20 + 2, 2):
#      print(whatevernumber)


# Exercise 3:
# Prompt the user for 3 numbers.
# Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing NUMBER1, NUMBER2, NUMBER3, and THEAVERAGE with the actual values.

# num1 = int(input("type a number"))
# num2 = int(input("type another number"))
# num3 = int(input("type one more number"))
# total = num1 + num2 + num3
# print(total)


# Challenge:
# Password Checker - Ask the user to enter a password.
# Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.

userinput = ""
while userinput != "Q":
    userinput = input("Enter a Password")
    if userinput == "Q":
        break
    userinput2 = input("Re-enter your password")
    if userinput2 == userinput:
        print("Correct!")
        break
    else:
        print("WRONG!")

















