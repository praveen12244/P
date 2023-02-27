npm=input("enter the name:")
print(npm[::-1])
if npm == npm[::-1]:
    print("it is palindrome")
else:
    print("it is  not a plaindrome")
    
print(npm[::2])
a=reversed(npm)
print(a)