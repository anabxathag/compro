"""devlab"""
def main():
    """tree christ"""
    num = int(input())
    bimai = []
    for i in range(num +1):
        laye = "*" * ((2 * i) + 1)
        bimai.append(laye)
    coe = 0
    while coe < num:
        ind = 0
        for i in bimai[: 2 + coe]:
            print((" " * (num - ind)) + i)
            ind += 1
        coe += 1
    print((" " * num) + "|")
    base = "=" * num
    print(base + "V" + base)
main()
