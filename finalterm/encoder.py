"""[Extra]"""
def main():
    """Easy - encoder"""
    messa = input().lower()
    direc = int(input())
    text = "abcdefghijklmnopqrstuvwxyz"
    news = ""
    for i in messa:
        ind = text.find(i) + direc
        if ind >= len(text):
            ind -= len(text) * abs(ind // len(text))
        elif ind < -1 * len(text):
            ind += len(text) * abs(ind // len(text))
        news += text[ind]
    print(news)
main()
