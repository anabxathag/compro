def addIntrrest(balance, rate):
    newBalance = balance * (1 + rate)
    return newBalance
def main():
    amount = 1000
    rate = 0.05
    amount = addIntrrest(amount, rate)
    print(amount)
main()
