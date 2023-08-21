"""Assignment4 Kor3"""
def main():
    """แสดงจำนวนคำที่รับเข้ามาที่ปรากฎอยู่ในไฟล์"""
    myfile = input()
    word = input()
    file = open(myfile, mode = 'r')
    text = ""
    for i in file:
        text += i
    nub = text.count(word)
    print(nub)
main()
