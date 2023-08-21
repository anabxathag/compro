"""multiple"""
def wanged(num):
    """calculate"""
    total = 1
    for i in range(num):
        total *= (365 - i) / 365
    return total
def main():
    """birthdays"""
    num = int(input())
    print(wanged(num))
main()
