"""[Pre-Midterm]"""
def main():
    """Thapster"""
    test = int(input())
    for _ in range(test):
        num_note = int(input())
        orgi_note = input().split()
        your_note = input().split()
        total = 0
        count = 0
        for i in range(num_note):
            if orgi_note[i] == your_note[i]:
                count += 1
                total += count
            else:
                count = 0
        print(total)
main()
