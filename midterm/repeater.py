"""devlab"""
def main():
    """Repeater"""
    text = input()
    liz = []
    for i in text:
        liz.append(i)
    for i in range(len(text)):
        print(" " * 2 * (len(text) - 1 - i), end="")
        laye = []
        for j in range(i + 1):
            laye.append(liz[j])
        laye.reverse()
        for k in range(len(laye)):
            print(laye[k], end=" ")
        laye.pop()
        laye.reverse()
        for l in range(len(laye)):
            print(laye[l], end=" ")
        print()
main()
