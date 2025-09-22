name = str(input("Enter your name:"))
surname = str(input("Enter your surname:"))

if(name.isspace() or len(name) == 0 or name.isalpha() != True):
    print("Error with firts name...")
elif(surname.isspace() or len(surname) == 0 or surname.isalpha() != True):
    print("Error with surname...")
else:
    first = name.strip()
    last = surname.strip()

    initials = name[0]+ surname 

    formatInitials = initials.lower()

    email = formatInitials  + "@greenegad.ac.uk"

    print(f"{name} {surname} {email}")


 


















































