"""[Extra]"""
def main():
    """Easy - ป้ายไฟ"""
    text = input().upper()
    frame = "|--" + ("-" * len(text)) + "--|"
    print(frame + "\n|", end="")
    print(text.center(len(frame) - 2, " "), end="")
    print("|\n" + frame)
main()
