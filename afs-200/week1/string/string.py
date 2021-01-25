# The string.py file should ask a user their “name” and “age”
# In the string.py file, write a code that Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input ("what is your name")
print (name)
age = input ("how old are you")
print (age)
year = 100 - int(age)
print (name + " in " + str(year) + " years you will turn 100 years old ")