print("------STUDENTDS NAMES MANAGER------")
print("=" * 50)

choice = 0
students = []

while choice != 5:
    
    print("1. Add student")
    print("2. Remove student")
    print("3. Search student")
    print("4. Show all students")
    print("5. Exit")
    
    
    choice = int(input("Enter a number from 1 - 5 to proceed : "))

    if choice == 1:
        name = input("Enter a name : ")
        students.append(name)
        print(f"List of students after adding new studnts {students}")
        
    elif choice == 2:
        name = input("Enter a name you want to remove: ")
        if name in students:
            students.remove(name)
            print(f"List of students after removing students {students}")
            
        else:
            print("Student not found!")  
            
    elif choice == 3:
        name = input("Enter a name you want to search for : ")
        
        if name in students:
            print(f"{name} was FOUND in the list")
        
        else:
            print(f"{name} was Not found in list")  
            
    elif choice == 4:
        if students:
            print(f"All the students are {students}")
        else:
            print("no student found")
            
    elif choice == 5:
        print("EXIT PROGRAM")   
    
    else:
        print("INVALID CHOICE ENTERED") 
    