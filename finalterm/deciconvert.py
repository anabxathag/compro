"""[Extra]"""
def main():
    """Intermediate - Decimal Converter"""
    numb = int(input())
    text = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(2, 37):
        tmp = numb
        ans = ""
        if tmp > 0:
            while tmp > 0:
                ans += text[tmp % i]
                tmp = int(tmp / i)
            print("Base {}: {}".format(i, ans[::-1]))
        else:
            print("Base {}: {}".format(i, 0))
main()
