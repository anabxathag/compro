"""[Pre-Midterm]"""
def fac(num):
    """Factorial"""
    if num <= 1:
        return 1
    else:
        return num * fac(num - 1)
def main():
    """Tile Again?"""
    kanat = int(input())
    perf = []
    sol = []
    for i in range(kanat):
        for j in range(kanat):
            if kanat == (3 * i) + (4 * j):
                for _ in range(i):
                    sol.append(3)
                for _ in range(j):
                    sol.append(4)
                perf.append(sol)
                sol = []
                break
    if len(perf) == 0:
        print("Nope")
    else:
        print("Yes")
        ans = 0
        for i in perf:
            sage = len(i)
            three = i.count(3)
            four = i.count(4)
            case = (fac(sage) / (fac(three) * fac(four)))
            ans += int(case)
        print(ans)
main()
