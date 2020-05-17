class Cal
  attr_reader :v1, :v2
  attr_writer :v1
  def initialize(v1,v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    return @v1+@v2
  end
  def subtract()
    return @v1-@v2
  end
  def setV1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
  end
  def setV2(v)
    if v.is_a?(Integer)
      @v2 = v
    end
  end
  def getV1()
    return @v1
  end
  def getV2()
    return @v2
  end
end
c1 = Cal.new(10,10)
p c1.add()
p c1.subtract()
c1.setV1('one')        #무시되는 코드
#c1.v1 = 'one'      #루비는 인스턴스에 직접접근 하는 방법을 제공하지 않기 때문에 에러가 나옴.
                    #만약 set메소드를 지워버린다면 v1 인스턴스 변수는 읽기만 가능함.
                    #루비는 훨씬 엄격하게 프로그래밍 하도록 유도되는 언어라는 것을 알 수 있음.

c1.v1 = 20
p c1.add()
c1.getV1()
