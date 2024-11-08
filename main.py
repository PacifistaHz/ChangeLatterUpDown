text=input("Enter a string: ")
newText=""
for i in text:
    if i.islower():
        newText=newText+i.upper()
    else:
        newText=newText+i.lower()
print(newText)