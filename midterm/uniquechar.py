"""[Pre-Midterm]"""
def main():
    """Unique Characters"""
    text = input()
    newtxt = ""
    tiz = []
    dni = set()
    while True:
        for i in text:
            tiz.append(i)
        for i in range(len(text)):
            if text[i : i + 2] == (text[i] * 2):
                dni.add(i)
                dni.add(i + 1)
        if len(dni) == 0:
            break
        for i in dni:
            tiz.pop(i)
            tiz.insert(i, "")
        for i in range(len(tiz)):
            newtxt += tiz[i]
        print(newtxt)
        clone = newtxt
        text = clone
        newtxt = ""
        tiz = []
        dni = set()
main()
