"""Week9 Exercise4"""
def cal_area(rad):
    """calculate area circle"""
    return 3.14 * (rad ** 2)
def cal_circumference(rad):
    """calculate circumference circle"""
    return 2 * 3.14 * rad
def main():
    """input radius circle"""
    radius = float(input("Enter radius of circle: "))
    area = cal_area(radius)
    circum = cal_circumference(radius)
    print("Area of this circle = " + str(area))
    print("circumference of this circle = " + str(circum))
main()
