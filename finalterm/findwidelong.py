"""[Extra]"""
def main():
    """Easy - Find Wide x Long"""
    dan = input()
    liz = []
    while dan != "end":
        liz.append(dan)
        dan = input()
    row, col = len(liz), liz[0].count("*")
    print("{} x {}".format(row, col))
main()
