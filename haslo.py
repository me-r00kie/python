print('Enter correct username and password combo to continue')
count = 0

# "" or '' because you are assigning a value string into it
password = ""
username = ""

# looping will continue when wrong input for three times and ask again...
while password!='Krol' and username!='Piotr' and count < 3:
    # you are collecting user input from CLI separately (you can not assign and operator to such operation as per your code ;)
    username = input("Enter username: ")
    password = input("Enter password: ")

    if password=='Krol' and username=='Piotr':
     # if match, grand and break
     print('Access granted')
     break

    else:
        print('Access denied. Try again.')
        count+=1     # as per gbse, in the comments, you will need the + to count up