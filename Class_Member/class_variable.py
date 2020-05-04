class Cs:
    #Cs.count = 0                   오류 발생. 클래스를 모두 읽기 전 까지는 클래스가 생성되지 않아서(?)
    count = 0                       #정의를 해줘야 함 (클래스에 소속된 클래스 변수 )

    def __init__(self):
        Cs.count = Cs.count + 1         #인스턴스가 생성될 때마다 생성자 호출되고 몇개의 인스턴스가 생성됐는지 카운트.
                                        #클래스 변수에 접근할 때에는 클래스네임을 통해 접근해야 한다.

    @classmethod
    def getCount(cls):                  #첫번째 인자 들어가야함. 이 인자는 클래스를 가르킨다.
        return Cs.count


i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()
print(Cs.getCount())
