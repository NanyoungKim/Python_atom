class Calculator(object):
    def __init__(self, v1, v2):    #self의 기능은? 파이썬에서는 첫번째 매개변수를 꼭 정의해야한다. 첫번째 매개변수는 언제나 그 인스턴스를 가리킨다.
        print(v1,v2)
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2


c1 = Calculator(10,10)
print(c1.add())
print(c1.subtract())

c2 = Calculator(30,20)
print(c2.add())
print(c2.subtract())
