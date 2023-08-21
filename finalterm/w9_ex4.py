def printName(name):
    print('Name : ' + name)
    name = 'Jack'
    # แม้ชื่อตัวแปรเหมือนกัน แต่ไม่สามารถเปลี่ยนค่าที่main()ได้
def main():
    name = 'Adam'
    printName(name)
    print('Name : ' + name)
main()
