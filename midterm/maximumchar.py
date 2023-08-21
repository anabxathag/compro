"""[Week 7]"""
def main():
    """Caesar Cypher"""
    text = input()
    lis_alp = []
    lis_num = []
    for i in text:
        if i not in lis_alp:
            lis_alp.append(i)
    for i in lis_alp:
        num = text.count(i)
        lis_num.append(num)
    for i in range(len(lis_num)):
        if lis_num[i] == max(lis_num):
            print(lis_alp[i], end="")
main()
