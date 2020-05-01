class Class1(object):
    def method1(self): return 'm1'
c1 = Class1()
print(c1, c1.method1())



class Class3(Class1):                   #Class1을 상속하면서 method1()을 쓸 수 있게 됨.
    def method2(self): return 'm2'
c3 = Class3()
print(c3, c3.method1())                 #Class3에 method1()없으니 부모 클래스인 Class1을 본다. 거기에 method1()있으므로 사용 가능. 
print(c3, c3.method2())



class Class2(object):
    def method1(self): return 'm1'     #Class1과 중복 발생.
    def method2(self): return 'm2'
c2 = Class2()
print(c2, c2.method1())
print(c2, c2.method2())
