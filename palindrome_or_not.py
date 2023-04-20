i = input("Enter the String:- ")

s = (i[::-1])
print(s)
# print(i[:: 1])
if s == i:
    print("---This String is Palindrome---")
else:
    print("---Not a palindrome---")
