"""Week9 Exercise6"""
def main():
    """calculate new salary n people"""
    stipend = [float(x) for x in input("Please enter stipends: ").split(",")]
    rate = [float(x) for x in input("Please enter rate: ").split(",")]
    bonus = float(input("Please enter bonus: "))
    output = new_stipend(stipend, rate, bonus)
    print(f'Previous stipend: {stipend}')
    print(f'Current stipend: {output}')
def new_stipend(amount, percent, extra):
    """Compute new stipend from rate and bonus"""
    new_sal = []
    for i in range(len(amount)):
        news = (amount[i] * (1 + (percent[i] / 100))) + extra
        new_sal.append(news)
    return new_sal
main()
