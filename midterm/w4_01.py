"""Assignment4 Kor1"""
def main():
    """เขียนข้อความนำเข้าจากผู้ใช้ต่อท้ายข้อมูลในไฟล์"""
    file_0 = open('names.txt', mode = 'r')
    text = ""
    for i in file_0:
        text += i
    text = text.replace('\n',',')
    data_1 = text[: 10]
    data_2 = text[11 : 27]
    data_3 = text[28 : 43]
    
    file_1 = open('names.txt', mode = 'w')
    mesa = input()
    file_1.write('%s' %data_1)
    file_1.write('\n%s' %data_2)
    file_1.write('\n%s' %data_3)
    file_1.write('\n%s' %mesa)
main()
