"""[Week 7]"""
def main():
    """Caesar Cypher"""
    text = input()
    ans = ""
    for i in range(len(text)):
        buo = chr(ord(text[i]) + 3)
        ans += buo
    print(ans)
main()
