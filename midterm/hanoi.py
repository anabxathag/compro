"""[Pre-Midterm]"""
def hanoi(num, one, two, three):
    """repeat"""
    if num == 0:
        return
    hanoi(num - 1, one, three, two)
    print(one, three)
    hanoi(num - 1, two, one, three)
def main():
    """Hanoi"""
    num = int(input())
    hanoi(num, 1, 2, 3)
main()
