"""[Extra]"""
def main():
    """Easy - Tuple's Sad life"""
    y2k = (input().split(" "))
    elemen = input()
    ind = y2k.index(elemen)
    con = y2k.count(elemen)
    for _ in range(con):
        for _ in range(con):
            print(ind, end=" ")
        print()
main()
