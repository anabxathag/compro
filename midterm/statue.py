"""[Week 6]"""
def main():
    """Statue"""
    moei = int(input())
    up_y = set()
    down_y = set()
    zero_y = set()
    zero_x = set()
    for _ in range(moei):
        posi = input()
        axis_x = float(posi[: posi.find(",")])
        axis_y = float(posi[posi.find(",") + 1 :])
        try:
            ongxa = axis_y / axis_x
            if axis_y > 0:
                up_y.add(ongxa)
            elif axis_y < 0:
                down_y.add(ongxa)
            else:
                if axis_x >= 0:
                    ongxa = "zero_plus"
                else:
                    ongxa = "zero_minus"
                zero_y.add(ongxa)
        except ZeroDivisionError:
            if axis_y >= 0:
                ongxa = "infi_plus"
            else:
                ongxa = "infi_minus"
            zero_x.add(ongxa)
    print(len(up_y) + len(down_y) + len(zero_x) + len(zero_y))
main()
