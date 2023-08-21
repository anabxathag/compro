"""Week10 Example2"""
# กำหนดความสามารถclass แบบที่1
class Cow:
    """atribute"""
    cid = 'C00000'
    gender = 'M'
    weight = 0
    age = (0, 0)
    def validID(self, cowID):
        """method"""
        if len(cowID) != 6:
            return False
        tmp = int(cowID[1:])
        if cowID[0] != "C":
            return False
        elif 0 <= tmp <= 99999:
            return True
        else:
            return False
sally = Cow()
sally.cid = "C00001"    # เปลี่ยนค่าคุณสมบัติ
sally.gender = "M"
sally.weight = 143.25
sally.age = (2, 10)
print("sally")
print(sally.validID(sally.cid))
print("ID = {}".format(sally.cid))
print("Gender = {}".format(sally.gender))
print("Weight = {}".format(sally.weight))
print("Age = {}".format(sally.age))
print()
poppy = Cow()
poppy.cid = "C00002"
poppy.gender = "F"
poppy.weight = 164.23
poppy.age = (2, 5)
print("poppy")
print(poppy.validID(poppy.cid))
print("ID = {}".format(poppy.cid))
print("Gender = {}".format(poppy.gender))
print("Weight = {}".format(poppy.weight))
print("Age = {}".format(poppy.age))
print()
jane = Cow()
jane.cid = "C00003"
jane.gender = "M"
jane.weight = 183.76
jane.age = (3, 6)
print("jane")
print(jane.validID(jane.cid))
print("ID = {}".format(jane.cid))
print("Gender = {}".format(jane.gender))
print("Weight = {}".format(jane.weight))
print("Age = {}".format(jane.age))
print(jane.validID("A000007"))
print()

# กำหนดความสามารถclass แบบที่2
class Chick:
    """atribute"""
    cid = 'C00000'
    gender = 'M'
    weight = 0
    age = (0, 0)
    def validID(self):
        """method"""
        if len(self.cid) != 6:
            return False
        tmp = int(self.cid[1:])
        if self.cid[0] != "C":
            return False
        elif 0 <= tmp <= 99999:
            return True
        else:
            return False
pepo = Chick()
pepo.cid = "C00002"
pepo.gender = "F"
pepo.weight = 164.23
pepo.age = (2, 5)
print(pepo.validID())       # ไม่ต้องใส่argument
print(Chick.validID(pepo))
    