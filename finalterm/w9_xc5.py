"""Week9 Exercise5"""
def is_prime(num):
    """return true if n is prime number, otherwise false."""
    for i in range(2, num + 1):
        count = 0
        for j in range(i):
            if j <= 1:
                pass
            if j >= 2 and (i % j == 0):
                count += 1
                break
        if count == 0 and i != 2:
            print("%d is prime number." %i)
def main():
    """find prime number"""
    num = int(input("Enter number: "))
    is_prime(num)
main()
