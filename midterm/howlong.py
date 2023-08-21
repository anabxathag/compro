"""[Week 7]"""
def main():
    """How long"""
    alp_1 = input()
    alp_22 = input()
    num_1 = ord(alp_1.upper())
    num_22 = ord(alp_22.upper())
    diff = num_22 - num_1
    print((diff * -1 * (diff < 0)) + (diff * (diff >= 0)))
main()
