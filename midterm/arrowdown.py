"""[Week 7]"""
def main():
    """Arrow Down"""
    num = int(input())
    print(((" " * (num - 1)) + "*\n" + (" " * (num - 1)) + "*"))
    for i in range(num):
        for j in range((2 * num) - 1):
            if j == num - 1:
                print("*", end='')
            elif i == j:
                print("*", end='')
            elif i + j == (2 * num) - 2:
                print("*", end='')
            else:
                print(" ", end='')
        print()
main()
