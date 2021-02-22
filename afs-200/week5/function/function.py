num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print (largest)

def string_cases(str):
    UPPER_CASE=0
    LOWER_CASE=0
    for char in str:
        if char.isupper():
           UPPER_CASE+=1
        elif char.islower():
           LOWER_CASE+=1
        else:
           pass
    print ("Original String : ", str)
    print ("Number of Upper case characters : ", UPPER_CASE)
    print ("Number of Lower case Characters : ", LOWER_CASE)

string_cases('Leaping Lizard')
