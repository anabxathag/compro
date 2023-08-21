"""[Extra]"""
def main():
    """Intermediate - Wildcard"""
    num = int(input())
    pattern = input().lower().split("*")
    chest = []
    for _ in range(num):
        word = input().lower()
        chest.append(word)
    for i in chest:
        if i[0 : len(pattern[0])] == pattern[0] \
            and i[len(i) - len(pattern[1]) : len(i)] == pattern[1]:
            if len(pattern[0]) + len(pattern[1]) > len(i):
                print("NO")
            elif len(pattern[0]) + len(pattern[1]) <= len(i):
                print("YES")
        else:
            print("NO")
main()
