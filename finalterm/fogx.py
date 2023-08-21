"""[Extra]"""
def main():
    """Easy - f(g(x)) g(f(x))"""
    num = int(input())
    f_f = (num ** 2) + (2 * num) + 1
    g_g = (num / 2) + 1
    print("{:.2f}".format((g_g ** 2) + (2 * g_g) + 1))
    print("{:.2f}".format((f_f / 2) + 1))
main()
