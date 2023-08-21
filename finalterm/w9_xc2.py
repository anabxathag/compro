"""Week9 Exercise2"""
def new_stripend(current, percen, addi):
    """calculate new salary"""
    new_salary = (current + (current * (percen / 100))) + addi
    return new_salary
def main():
    """1 people"""
    stripend, rate, bonus = float(input()), float(input()), float(input())
    ans = new_stripend(stripend, rate, bonus)
    print(ans)
main()
