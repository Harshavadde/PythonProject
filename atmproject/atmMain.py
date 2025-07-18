#atmMain.py
from atmdevelop import DepositError, WithdrawAmountError, InSuffFundError
from atmmenu import menu
from atmoperation import deposit, Withdraw, balanceEnq
while(True):
    try:
        menu()
        ch=int(input("Enter ur choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDon't Deposit -Ve amd Zero Values")
                except ValueError:
                    print("\tDont Try to deposit alnums,strs and symbols")
            case 2:
                try:
                    Withdraw()
                except WithdrawAmountError:
                    print("\tDon't Withdraw -Ve amd Zero Values")
                except ValueError:
                    print("\tDont Try to deposit alnums,strs and symbols")
                except InSuffFundError:
                    print("\tUr Account does not contains Funds")
            case 3:
                balanceEnq()
            case 4:
                print("Thx for using this Project")
                break
            case _:
                print("\tUr Selection of Operation is wrong-try again")
    except ValueError:
        print("\tDon't enter alnums,strs and symbols for Choice--try again")

