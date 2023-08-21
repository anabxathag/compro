import random
"""Week9 Exercise1"""
def create_uname(fir, sur):
    """Username"""
    fir = fir[0].lower()
    sur = sur[:5].capitalize()
    username = fir + sur
    return username
def create_password(fir, sur):
    """Password"""
    num = ""
    fns = list(fir + sur)
    random.shuffle(fns)
    text = "".join(fns[0:6])
    for _ in range(3):
        num += str(random.randint(0,10))
    return text + num
def main():
    """Main Func"""
    fname = input("Enter your firstname: ")
    sname = input("Enter your surname: ")
    uname = create_uname(fname, sname)
    keys = create_password(fname, sname)
    print(uname)
    print(keys)
main()