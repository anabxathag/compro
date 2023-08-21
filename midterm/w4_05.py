"""Assignment4 Kor5"""
def main():
    """สร้าง username"""
    file_0 = open('firstname.txt', mode = 'r')
    us_id = []
    fr_name = []    # ชื่อพิมพ์เล็ก
    for i in file_0:
        num = ""
        first = ""
        for j in i:
            if j.isnumeric():
                num += j
            if j.isalpha():
                first += j.lower()
        us_id.append(num)
        fr_name.append(first)  
    uxui = []   # เลขท้าย39ของเลขประจำตัว
    for i in us_id:
        con = 0
        ide = ""
        for j in i:
            if con > 4:
                ide += j
            con += 1
        uxui.append(ide)
    
    file_1 = open('lastname.txt', mode = 'r')
    la_name = []
    for i in file_1:
        last_1 = ""
        for j in i:
            if j.isalpha():
                last_1 += j
        la_name.append(last_1)
    las_me = []     # นามสกุล6ตัวแรก พิมพ์ใหญ่ตัวแรกสุด ที่เหลือตัพิมพ์เล็ก
    for i in la_name:
        a = i.capitalize()
        last_22 = ""
        con = 0
        for j in a:
            if con < 6:
                last_22 += j
            else:
                break
            con += 1
        las_me.append(last_22)
    
    file_2 = open('username.txt', mode = 'w')
    for i in range(len(las_me)):
        file_2.write("%s%s%s\n" %(fr_name[i], las_me[i], uxui[i]))
main()
