num = input("please insert a number:")
print("The number is: " +num)
def double(number):
    return number * 2

print(double(int(num)))

if int(num) % 2 == 0:
    print ("even")# even

else: 
    print ("odd")# odd