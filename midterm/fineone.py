"""[Week 7]"""
def main():
    """fine one"""
    stick = int(input())
    bi_txt = input()
    points = 0
    for i in range(len(bi_txt)):
        if bi_txt[i : i + stick] == ("1" * stick):
            points += 1
    print(points)
main()
