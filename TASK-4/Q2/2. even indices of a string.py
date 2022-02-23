print("to find the characters at even indices of a string")
string = input("enter the string : ")
i = 0
even_string = ""
while i < len(string):
    if i % 2 == 0:
        even_string = (even_string + string[i])
    i += 1
print(even_string)
