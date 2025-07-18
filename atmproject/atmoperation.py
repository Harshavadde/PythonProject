#atmoperation.py
from atmdevelop import DepositError,WithdrawAmountError,InSuffFundError
bal=500.00
def deposit():
    damt=float(input("Enter Deposit Amount:"))
    if damt<=0:
        raise DepositError
    else:
        global bal
        bal+=damt
        print("\tUr Account xxxxxxxxxxxx123 Credited with INR:{}".format(damt))
        print("\tUr Account xxxxxxxxxxxx123 Balance after Deposit INR:{}".format(bal))

def Withdraw():
    global bal
    wamt=float(input("Enter Withdraw Amount:"))
    if wamt<=0:
        raise WithdrawAmountError
    elif((wamt+500)>=bal):
        raise InSuffFundError
    else:
        bal-=wamt
        print("\tUr Account xxxxxxxxxxxx123 Debited with INR:{}".format(wamt))
        print("\tUr Account xxxxxxxxxxxx123 Balance after Withdraw INR:{}".format(bal))

def balanceEnq():
    print("\tUr Account xxxxxxxx123 Balance with INR:{}".format(bal))