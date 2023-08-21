"""[Extra]"""
def main():
    """Intermediate - Vertical Histogram"""
    text = input().upper()
    barh = []
    for i in text:
        if (i.isalpha()) and (i not in barh):
            barh.append(i)
    barh.sort()
    for i in barh:
        print("{}: {}".format(i, "#" * text.count(i)))
main()
