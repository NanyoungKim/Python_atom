class C(object):
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)


c1 = C(10)
#print(c1.__value)    에러 뜸. under bar 2개 붙으면 외부에서 접근하는 것 금지됨.
c1.show()
