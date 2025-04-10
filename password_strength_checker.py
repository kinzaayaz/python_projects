import string
password = input("Enter your password: ")

x = string.ascii_letters  
y = string.digits         
z = string.punctuation    
has_letter = False
has_digit = False
has_special = False

for char in password:
    if char in x:
        has_letter = True
    if char in y:
        has_digit = True
    if char in z:
        has_special = True
        
if has_letter and has_digit and has_special:
    print("Password is strong")

elif has_letter and has_digit:
    print("Password is medium")

elif has_letter:
    print("Password is weak")
else:
    print("Password is very weak")
