#EmployeeDelete.py
import pickle
def deleteemployee():
    records = []
    with open("empinfo.pick", "rb") as fp:
        while (True):
            try:
                record = pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    found = False
    # accept New Salary for Updating based on emp number
    eno = int(input("Enter Employee Number for deleting record:"))
    for index in range(len(records)):
        if (records[index][0] == eno):
            found = True
            recindex = index
            break
    print("-"*50)
    if found:
        records.pop(recindex)
        with open("empinfo.pick","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmployee Record Removed--Verify")
    else:
        print("\tEmployee Records does no Exit to delete")
    print("-" * 60)