"""[Week 7]"""
def main():
    """The Weakest Characters"""
    charac = input()
    str_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if charac in str_char:
        num = str_char.find(charac)
        vilage = ""
        for i in range(num + 1):
            vilage += str_char[i]
        down = []
        floor = ""
        for i in range(len(vilage)):
            print(" " * (len(vilage) - i - 1), end="")
            floor += " " * (len(vilage) - i - 1)
            if i == 0:
                print(vilage[i])
                floor += vilage[i]
                down.append(floor)
            else:
                print(vilage[: i + 1] + vilage[i - 1 :: -1])
                floor += vilage[: i + 1] + vilage[i - 1 :: -1]
                down.append(floor)
            floor = ""
        down.pop()
        down.reverse()
        for i in down:
            print(i)
    else:
        print(charac)
main()
