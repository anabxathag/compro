"""[Extra]"""
def main():
    """Easy - Condition Mod"""
    num = int(input())
    if num % 2 != 0:
        print("Oooo")
    elif num == 2 or num == 4:
        print("lelelel")
    elif num % 2 == 0 and (6 <= num <= 20):
        print("OMG!")
    elif num % 2 == 0 and (num > 20):
        print("Infinite!")
    else:
        print("Out of condition!")
main()
