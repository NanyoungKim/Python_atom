class C1():
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("C1 m")

class C2():
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("C2 m")

class C3(C2, C1):
    def m(self):
        print("C3 m")

c = C3()
c.c1_m()
c.c2_m()
c.m()                   #C3_m 출력됨
print(C3.__mro__)       #__mro__라는 특수한 변수를 이용하여 우선순위를 보여준다.
