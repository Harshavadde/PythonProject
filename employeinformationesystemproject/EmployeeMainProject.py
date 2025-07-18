#EmployeeMainProject.py
from EmpMenu import menu
from EmployeeAdd import addemployee
from EmployeeDelete import deleteemployee
from EmployeeSearch import searchemployee
from EmployeeUpdate import updateemployee
from EmployeeView import viewallemployee,viewemployee
while(True):
    menu()
    try:
        ch=int(input("Enter Your Choice:"))
        match(ch):

            case 1:
                addemployee()
            case 2:
                deleteemployee()
            case 3:
                updateemployee()
            case 4:
                viewemployee()
            case 5:
                viewallemployee()
            case 6:
                searchemployee()
            case 7:
                print("Thanks for using this project")
                break
            case _:
                print("Ur Selection of Operation is Invalid--try again")
    except ValueError:
        print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR CHOICE-TRY AGAIN")