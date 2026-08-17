patients = [
    {"id": 1, "name": "Ali", "email": "ali@gmail.com"},
    {"id": 2, "name": "Sara", "email": "sara@gmail.com"},
    {"id": 3, "name": "Ahmed", "email": "ali@gmail.com"},
    {"id": 4, "name": "Usman", "email": "usman@gmail.com"},
    {"id": 5, "name": "Hina", "email": "ali@gmail.com"}
]
count = {} #Email count kara ga

for p in patients:
    email = p["email"]
    if email in count:
        count[email] += 1
    else:
        count[email] = 1

print("Duplicate Emails:") #PRINT DUPLICATE EMAILS

for email in count:
    if count[email] > 1:
        print(email, count[email], "times")

unique = {} #Duplicate records remove kara 
for p in patients:
    email = p["email"]
    if email not in unique:
        unique[email] = p    #Pehli row save karo

    
    elif p["id"] < unique[email]["id"]: #Agar new ID choti hai to usko save karo
        unique[email] = p

patients = list(unique.values()) #Final list
print(" Final Patients:")
for p in patients:
    print(p)