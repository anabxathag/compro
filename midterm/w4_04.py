"""Assignment4 Kor4"""
def main():
    """แสดงจำนวนบรรทัดจากชื่อไฟล์ที่รับจากผู้ใช้"""
    myfile = input()
    file = open(myfile, mode = 'r')
    nub = len(file.readlines())
    print(nub)
main()
