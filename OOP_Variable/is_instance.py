class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):   #isistnace  :v1이 int(파이썬에 내장되어 있는 클래스)의 인스턴스인지 체크하는 함수.
            self.v1 = v1                    #맞으면 true, 아니면 false를 리턴한다.
        if isinstance(v2, int):             # 인스턴스 변수가 원하지 않는 값으로 더럽혀지는 것을 방지한다.
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1



c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1('one')
#c1.v1 = 'one'    파이썬은 이렇게 직접 접근하는 것을 막을 수는 없다. 이 객체를 올바르게 잘 사용할 것이라고 기대하는 미덕의 파이썬

c1.v2 = 30
print(c1.add())
print(c1.subtract())
