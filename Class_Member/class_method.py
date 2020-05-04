class Cs:
    @staticmethod                    #장식자를 붙여줌으로써 이 메소드가 클래스에 속한 클래스 멤버라는 것을 알려줌.
    def static_method():
        print("Static method")


    @classmethod
    def class_method(cls):          #클래스 메소드는 cls라는 첫번째 매개변수가 있어야한다. (함수 이름 바꿔도 됨.)
        print("Class method")

    def instance_method(self):
        print("Instance method")


i = Cs()
#클래스메소드
Cs.static_method()
Cs.class_method()

#인스턴스 메소드
i.instance_method()
