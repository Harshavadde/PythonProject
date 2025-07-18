#EmployeeView.py
import pickle
def viewemployee():
    records=[]
    with open("empinfo.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    eno=int(input("Enter Employee Number to view details:"))
    found=False
    for record in records:
        if(record[0]==eno):
            found=True
            rec=record
            break
    print("-"*50)
    if found:
        print("\tEmployee Number:{}".format(rec[0]))
        print("\tEmployee Name:{}".format(rec[1]))
        print("\tEmployee Salary:{}".format(rec[2]))
    else:
        print("\tEmployee Number {} does not exist".format(eno))
    print("-"*50)

def viewallemployee():
    try:
        with open("empinfo.pick", "rb") as fp:
            print("-" * 50)
            print("\tENO\t\tNAME\tSAL")
            print("-" * 50)
            while (True):
                try:
                    record = pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val), end="  ")
                    print()
                except EOFError:
                    print("-" * 40)
                    break
    except FileNotFoundError:
        print("File doesn't exist")