"""[Extra]"""
def main():
    """Hard - Traveller"""
    route = input().upper()
    x_pikut, y_pikut = [0], [0]
    for i in range(len(route)):
        if route[i] == "W":
            y_pikut.append(y_pikut[i] - 1)
            x_pikut.append(x_pikut[i])
        elif route[i] == "S":
            y_pikut.append(y_pikut[i] + 1)
            x_pikut.append(x_pikut[i])
        elif route[i] == "D":
            x_pikut.append(x_pikut[i] + 1)
            y_pikut.append(y_pikut[i])
        elif route[i] == "A":
            x_pikut.append(x_pikut[i] - 1)
            y_pikut.append(y_pikut[i])
    y_low = abs(min(y_pikut))
    x_low = abs(min(x_pikut))
    ku_xy = []
    for i in range(len(y_pikut)):
        x_pikut[i] += x_low
        y_pikut[i] += y_low
        ku_xy.append([x_pikut[i], y_pikut[i]])
    for i in range(max(y_pikut) + 1):
        for j in range(max(x_pikut) + 1):
            tumneng = [j, i]
            if tumneng == ku_xy[0]:
                print("B", end=" ")
            elif tumneng == ku_xy[len(ku_xy) - 1]:
                print("E", end=" ")
            elif tumneng in ku_xy:
                print("O", end=" ")
            else:
                print("-", end=" ")
        print()
main()
