"""[Extra]"""
def main():
    """Easy - daysCount"""
    tim_liz = input().split("/")
    tim_liz = [int(i) for i in tim_liz]
    month, day, year = tim_liz[0], tim_liz[1], tim_liz[2]
    text = '{:02d}/{:02d}/{} is '.format(month, day, year)
    wan = (31 * (month - 1)) + day - ((((4 * month) + 23) // 10) * (month >= 3))
    pref = ['st', 'nd', 'rd', 'th']
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        if month >= 3:
            wan += 1
        else:
            pass
        sufx = pref[wan % 10 - 1 - (1 * (wan % 10 - 4) * (wan % 10 > 4))]
        text += 'the {}{} days of the year'.format(wan, sufx)
    else:
        if (month == 2) and (day == 29):
            text += 'invalid'
        else:
            sufx = pref[(wan % 10) - 1 - (1 * ((wan % 10) - 4) * ((wan % 10) > 4))]
            text += 'the {}{} days of the year'.format(wan, sufx)
    print(text)
main()
