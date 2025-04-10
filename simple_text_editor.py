filename=input("Enter file name to open or create: ")
text=[]
try:
    f=open(filename,"r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print(filename,"not found. Creating a new file.")
print("Enter your text (Type 'SAVE' on new line to save and exit: )")

while True:
    text_data=input()
    if text_data=="SAVE":
        break
    else:
        text.append(text_data)

with open(filename,"a")as f:
    f.write("\n".join(text))

    
    
    