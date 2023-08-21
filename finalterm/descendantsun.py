"""[Extra]"""
import math
def main():
    """Hard - Descendants of the Sun"""
    num = int(input())
    gan_x, gan_y = [], []
    for _ in range(num + 1):
        pikut = input()
        pi_x = float(pikut[1 : pikut.find(",")])
        pi_y = float(pikut[pikut.find(",") + 1 : len(pikut) - 1])
        gan_x.append(pi_x)
        gan_y.append(pi_y)
    for i in range(num):
        begin = [gan_x[i], gan_y[i]]
        end = [gan_x[i + 1], gan_y[i + 1]]
        dis = 2 * 6378.137 * \
            math.asin(((math.sin(((end[0] - begin[0]) / 2) * (3.1416 / 180)) ** 2) \
            + (math.cos(begin[0] * (3.1416 / 180)) * math.cos(end[0] * (3.1416 / 180)) * \
            (math.sin(((end[1] - begin[1]) / 2)  * (3.1416 / 180)) ** 2))) ** 0.5)
        direc = ""
        if begin[0] > end[0]:
            direc += "S"
        elif begin[0] < end[0]:
            direc += "N"
        if begin[1] > end[1]:
            direc += "W"
        elif begin[1] < end[1]:
            direc += "E"
        print("#{} Distance: {:.2f}km Direction: {}".format(i + 1, dis, direc))
main()
