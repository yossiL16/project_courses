from db.queries import *
from db.load_csv import *

def print_menu():
    print(
    """"
    --------------------
    what is your choice?
    --------------------

    1) Load csv.
    
    2) Search Records by Institution Name.
    
    3) Search Records by Course Name.
    
    4) Find Most Common Course.
    
    5) Find least Common Course.
    
    6) Show Course Count per District.
    
    7) Free SQL Query. 
    
    8) EXIT
    """)

while True:
    print_menu()
    choice = int(input("Choose option: "))
    if choice == 1:
        load_csv()
        continue
    elif choice == 2:
        search_Records_by_Institution_Name()
        continue
    elif choice == 3:
        search_Records_by_Course_Name()
    elif choice == 4:
        find_Most_Common_Course()
    elif choice == 5:
        find_least_Common_Course()
    elif choice == 6:
        show_Course_Count_per_District()
    elif choice == 7:
        free_SQL_Query()
    elif choice == 8:
        print("Thank you")
        print("We would love to see you again")
        break
    else:
        print("You made an error. Please enter only a correct number.")
