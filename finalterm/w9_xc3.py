"""Week9 Exercise3"""
def new_stripend(current, percen, addi):
    """calculate new salary"""
    new_sarlary = (current + (current * (percen / 100))) + addi
    return  new_sarlary
def main():
    """>=2 people"""
    stripend = input().split(",")
    rate = input().split(",")
    bonus = input()
    ans = []
    for i in range(len(rate)):
        news = new_stripend(float(stripend[i]), float(rate[i]), float(bonus))
        ans.append(news)
    print(stripend)
    print(ans)
main()
