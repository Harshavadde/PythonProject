#EmployeeSearch.py
import pickle
def searchemployee():
    try:
        records = []
        with open("empinfo.pick", "rb") as fp:
            while (True):
                try:
                    record = pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
        eno = int(input("Enter Employee Number to Searching details:"))
        found = False
        for record in records:
            if (record[0] == eno):
                found = True
                break
        print("-" * 50)
        if found:
            print("\t Valid Employee")
        else:
            print("\t Invalid Employee")
        print("-" * 50)
    except ValueError:
        print("DON'T ENTER ALNUMS,STRS AND SYMBOLS---TRY AGAIN")