"""[Extra]"""
def main():
    """Intermediate - TimeConverter"""
    hour = int(input())
    minute = int(input())
    if hour >= 12 and (hour // 12) % 2 == 0:
        hour -= 12 * (hour // 12)
        print("{:02d}:{:02d} AM".format(hour, minute))
    elif hour >= 12 and (hour // 12) % 2 != 0:
        hour -= 12 * (hour // 12)
        print("{:02d}:{:02d} PM".format(hour, minute))
    elif hour < 12:
        print("{:02d}:{:02d} AM".format(hour, minute))
main()
