"""Assignment4 Kor2"""
def main():
    """เขียนชุดคะแนนที่รับจากผู้ใช้ 1คแนนต่อ1บรรทัด"""
    mypoint = input()
    temp = mypoint.replace(",","\n")
    file = open('scores.txt', mode = 'w')
    file.write("%s" %temp)
main()
