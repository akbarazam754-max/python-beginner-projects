print("------THIS IS CONTACT BOOK------")
print("=" * 50)

choice = 0
contacts = {}

while choice != 5:
    
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Search contact")
    print("4. Show all contact")
    print("5. Exit")
    
    choice = int(input("Enter a number from 1 - 5 to proceed : "))
    
    if choice == 1:
        name = input("Enter name : ")
        contact = input("Enter 13 digit phone number : ")
        
        contacts[name] = contact
        print(contacts)
        
    elif choice == 2:
        name = input("Enter a name to remove contact: ")
        if name in contacts:
            del contacts[name]
            print(contacts)
        
        else:
            print("CONTACT NOT FOUND")
            
    elif choice == 3:
        name = input("Enter a name you want to search contact: ")
        if name in contacts:
            print(contact)
            
        else:
            print("contact not found")
            
    elif choice == 4:
        if contacts:
            print(f"this is the list of all contacts {contacts}")
            
        else:
            print("contacts not found")
            
    elif choice == 5:
        print("EXIT")
        
    else:
        print("invalid choice entered")
    
    