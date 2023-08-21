"""[Extra]"""
def main():
    """Intermediate - Aladin & The Magic Burger"""
    order = input().lower()
    starch = len(order) % 10
    meat = order.find("burger")
    print(("(|" * starch) + ("{}" * meat) + ("|)" * starch))
main()
