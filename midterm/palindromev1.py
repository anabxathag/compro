"""[Week 7]"""
def main():
    """PalindromeV1"""
    text_og = input()
    lis_txt = []
    for i in text_og:
        lis_txt.append(i)
    lis_txt.reverse()
    text_rev = ""
    for i in lis_txt:
        text_rev += i
    if text_rev == text_og:
        print("YES")
    else:
        print("NO")
main()
