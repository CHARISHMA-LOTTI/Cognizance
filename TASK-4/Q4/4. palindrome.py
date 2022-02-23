print("to check if a number is palindrome or not")
n = input("enter the number : ")
number = int(n)
t = number
reverse = 0
while t > 0:
    i = int(t % 10)
    reverse = (reverse * 10) + i
    t = int(t / 10)
if reverse == number:
    print("True")
else:
    print("False")
