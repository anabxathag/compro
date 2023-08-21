"""[Extra]"""
import math
def main():
    """Intermediate - Walking average distance"""
    num = int(input())
    avg = 0
    dean = []
    for _ in range(num):
        walk = int(input())
        avg += walk
        dean.append(walk)
    avg /= num
    for i in dean:
        print(math.ceil(abs(i - avg)))
main()
