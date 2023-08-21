import random
"""Week10 Exercise1"""
class Paperback:
    """Kor 1"""
    def __init__(self, prinlen, dimen, weight):
        """constructor method"""
        self.prinlen = prinlen
        self.dimen = dimen
        self.weight = weight
    def sample(self):
        """สุ่มเลขหน้าหนังสือ 10หน้าติดกัน"""
        sam = random.randint(1, self.prinlen)
        print("สุ่มได้หน้าดังนี้ : ", end="")
        if sam > self.prinlen - 10:
            for i in range(sam - 10, sam):
                print(i, end=" ")
        else:
            for i in range(sam, sam + 10):
                print(i, end=" ")
        print()
    def CalShipping(self):
        """คำนวณค่าหนังสือ"""
        if float(self.dimen[: self.dimen.find("x")]) * float(self.dimen[self.dimen.find("x") + 1 :]) >= 1000:
            print("ค่าส่งหนังสือ = %.2f บาท" %((self.weight * 0.25) + 20))
        elif float(self.dimen[: self.dimen.find("x")]) * float(self.dimen[self.dimen.find("x") + 1 :]) < 1000:
            print("ค่าส่งหนังสือ = %.2f บาท" %(self.weight * 0.1))
class Ebook:
    """Kor 2"""
    def __init__(self, fiesiz, prinlen, curpag):
        """constructor method"""
        self.fiesiz = fiesiz
        self.prinlen = prinlen
        self.curpag = curpag
    def sample(self):
        """สุ่มเลขหน้าหนังสือ 10หน้าติดกัน"""
        sam = random.randint(1, self.prinlen)
        print("สุ่มได้หน้าดังนี้ : ", end="")
        if sam > self.prinlen - 10:
            for i in range(sam - 10, sam):
                print(i, end=" ")
        else:
            for i in range(sam, sam + 10):
                print(i, end=" ")
        print()
    def CalShipping(self):
        """คำนวณค่าหนังสือ"""
        if self.fiesiz >= 100:
            print("ค่าส่งหนังสือ = %.2f บาท" %((self.fiesiz * 0.25) + 20))
        elif self.fiesiz < 100:
            print("ค่าส่งหนังสือ = %.2f บาท" %(self.fiesiz * 0.1))
    def Goto(self, page):
        """คืนค่า True หรือ False จาก page"""
        if 1 <= page <= self.prinlen:
            print("True")
        else:
            print("False")
    def NextPage(self):
        """คืนค่าเลขหน้าถัดไป"""
        page = self.curpag + 1
        print("หน้าถัดไป = ", end="")
        self.Goto(page)
    def PreviousPage(self):
        """คืนค่าเลขหน้าก่อนหน้า"""
        page = self.curpag - 1
        print("หน้าก่อนหน้า = ", end="")
        self.Goto(page)
class AudioBook:
    """Kor 3"""
    def __init__(self, lislen, fiesiz, curtim):
        """constructor method"""
        self.lislen = lislen
        self.fiesiz = fiesiz
        self.curtim = curtim
    def sample(self):
        """สุ่มเลขช่วงเวลา2ช่วง ห่างกัน10วินาที"""
        minute = random.randint(0, int(self.lislen[: self.lislen.find(":")]))
        second, mm_1, ss_1, mm_2, ss_2 = 0, minute, 0, 0, 0
        if minute == int(self.lislen[: self.lislen.find(":")]):
            second = random.randint(0, int(self.lislen[self.lislen.find(":") + 1 :]))
            ss_1 = second
            if ss_1 >= int(self.lislen[self.lislen.find(":") + 1 :]) - 10:
                ss_2 = ((ss_1 - 10) * (ss_1 - 10 >= 0)) + ((ss_1 + 50) * (ss_1 - 10 < 0))
                mm_2 = (mm_1 * (ss_1 - 10 >= 0)) + ((mm_1 - 1) * (ss_1 - 10 < 0))
            elif ss_1 < int(self.lislen[self.lislen.find(":") + 1 :]) - 10:
                ss_2 = ss_1 + 10
                mm_2 = mm_1
        elif minute != int(self.lislen[: self.lislen.find(":")]):
            second = random.randint(0, 59)
            ss_1 = second
            ss_2 = ((ss_1 + 10) * (ss_1 + 10 <= 59)) + ((ss_1 - 50) * (ss_1 + 10 > 59))
            mm_2 = (mm_1 * (ss_1 + 10 <= 59)) + ((mm_1 + 1) * (ss_1 + 10 > 59))
        print("สุ่มได้เวลาดังนี้ => ", end="")
        print(str(mm_1) + ":" + str(ss_1) + " " + str(mm_2) + ":" + str(ss_2))
    def CalShipping(self):
        """คำนวณค่าหนังสือ"""
        if self.fiesiz >= 100:
            print("ค่าส่งหนังสือ = %.2f บาท" %((self.fiesiz * 0.25) + 20))
        elif self.fiesiz < 100:
            print("ค่าส่งหนังสือ = %.2f บาท" %(self.fiesiz * 0.1))
    def Play(self):
        """เล่นตั้งแต่เวลาปจบ. ถึง (15วิข้างหน้า or printlength)"""
        c_mm = int(self.curtim[: self.curtim.find(":")])
        c_ss = int(self.curtim[self.curtim.find(":") + 1 :])
        print("เล่นเวลาได้ดังนี้ => ", end="")
        if (c_mm == int(self.lislen[: self.lislen.find(":")])) and (c_ss > int(self.lislen[self.lislen.find(":") + 1 :]) - 14):
            for i in range(int(self.lislen[self.lislen.find(":") + 1 :]) - c_ss):
                print(str(c_mm) + ":" + str(c_ss + i), end=" ")
        elif (c_mm == int(self.lislen[: self.lislen.find(":")])) and (c_ss <= int(self.lislen[self.lislen.find(":") + 1 :]) - 14):
            for i in range(15):
                print(str(c_mm) + ":" + str(c_ss + i), end=" ")
        elif c_mm != int(self.lislen[: self.lislen.find(":")]):
            for i in range(15):
                bug_mm = c_mm
                bug_ss = c_ss
                bug_ss = ((c_ss + i) * ((c_ss + i) <= 59)) + ((c_ss + i - 60) * ((c_ss + i) > 59))
                bug_mm = (c_mm * ((c_ss + i) <= 59)) + ((c_mm + 1) * ((c_ss + i) > 59))
                print(str(bug_mm) + ":" + str(bug_ss), end=" ")
        print()
def main():
    """main func"""
    random.seed(10)
    print("***** Kor 1 *****")
    b_1 = Paperback(250, "30x35", 25)
    b_1.sample()
    b_1.CalShipping()
    b_2 = Paperback(124, "20x25", 20)
    b_2.sample()
    b_2.CalShipping()
    b_3 = Paperback(565, "35x40", 35)
    b_3.sample()
    b_3.CalShipping()
    print("\n***** Kor 2 *****")
    b_2 = Ebook(128, 224, 100)
    b_2.sample()
    b_2.CalShipping()
    b_2.NextPage()
    b_2.PreviousPage()
    b_2 = Ebook(72, 156, 1)
    b_2.sample()
    b_2.CalShipping()
    b_2.NextPage()
    b_2.PreviousPage()
    b_2 = Ebook(90, 178, 178)
    b_2.sample()
    b_2.CalShipping()
    b_2.NextPage()
    b_2.PreviousPage()
    print("\n***** Kor 3 *****")
    b_3 = AudioBook("25:45", 224, "25:40")
    b_3.sample()
    b_3.CalShipping()
    b_3.Play()
    b_3 = AudioBook("25:45", 196, "25:00")
    b_3.sample()
    b_3.CalShipping()
    b_3.Play()
    b_3 = AudioBook("5:45", 75, "4:50")
    b_3.sample()
    b_3.CalShipping()
    b_3.Play()
main()
