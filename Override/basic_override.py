class C1:
    def m(self):
        return 'parent'
class C2(C1):
    def m(self):
        #return 'child'                     #하고 아래에서 print(o.m()) 하면 그냥 child 출력됨.
        return super().m() + ' child'       #super().m()은 부모의 함수를 가리킨다.
    pass                                    #메소드가 존재하지 않는 클래스를 실행시킬 때 안에 써주는 것.


o = C2()
print(o.m())
