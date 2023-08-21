"""[Week 7]"""
def main():
    """2D Distance"""
    x_1 = float(input())
    y_1 = float(input())
    x_2 = float(input())
    y_2 = float(input())
    dis = (((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)) ** 0.5
    print("Distance = %.3f" %dis)
main()
