"""[Extra]"""
def main():
    """Hard - Cards Shuffling"""
    num = int(input())
    dex = []
    for _ in range(num):
        card = int(input())
        dex.append(card)
    count = 0
    ans = dex.copy()
    ans.sort()
    while dex != ans:
        for i in range(len(dex) - 1):
            if dex[len(dex) - 1] <= dex[i]:
                last = dex[len(dex) - 1]
                dex.remove(last)
                dex.insert(i, last)
                count += 1
                break
            elif dex[i + 1] < dex[i] and i < len(dex) - 2:
                last = dex[len(dex) - 1]
                dex.remove(last)
                dex.insert(i + 1, last)
                count += 1
                break
    print(count)
main()
