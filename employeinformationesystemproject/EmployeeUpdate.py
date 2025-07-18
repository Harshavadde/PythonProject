#EmployeeUpdate.py
import pickle
def updateemployee():
    records = []
    with open("empinfo.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    # accept New Salary for Updating based on emp number
    eno = int(input("Enter Employee Number to updating salary:"))
    found = False
    for record in records:
        if (record[0] == eno):
            found = True
            rec=record
            break
    if found:
        sal = float(input("Enter Employee New Salary for Updating:"))
        rec[2]=sal
        with open("empinfo.pick","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmp Salary Updated--verify")
    else:
        print("\tEmployee Number {} does not exist".format(eno))