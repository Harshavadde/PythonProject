#EmployeeAdd.py
import pickle,sys
sys.path.append("C:\\Users\\iamha\\PycharmProjects\\6pmNestedloops\\ExceptionsExample")
from hittingValidation import validation
from developValidation import NameLengthError,SpaceError,InvalidNameError
def addemployee():
    with open("empinfo.pick","ab") as fp:
        while(True):
            try:

                print("-" * 50)
                # read the Student Values from KBD
                eno = int(input("Enter Student Number:"))
                ename =validation(input("Enter Student Name:"))
                sal = float(input("Enter Student Marks:"))
                # create an object of list
                lst = list()
                # Add the Values of student to lst
                lst.append(eno)
                lst.append(ename)
                lst.append(sal)
                # Save Iterable Object data into the file
                pickle.dump(lst, fp)
                print("\tEmployee Records saved in File Successfully")
                print("-" * 50)
                ch=input("Do u want to Insert Another Emp Record(yes/no):")
                if(ch.lower=="no"):
                    break
            except ValueError:
                print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR ENO AND EMP SAL--TRY AGAIN")
            except NameLengthError:
                print("\tPlz Enter Ur Name--try again ")
            except SpaceError:
                print("\tDon't Enter Space for Name--try again")
            except InvalidNameError:
                print("\t'{}' Invalid Name-try again".format(ename))
            else:
                print("\t'{}' is valid Name".format(ename))
                break

