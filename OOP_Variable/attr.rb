class C
  #attr_reader :value         #value라는 인스턴스 변수를 읽기 가능한 속성으로 (get메소드 없이도)
  #attr_writer :value         #value라는 인스턴스 변수를 수정 가능한 속성으로 (set메소드 없이도)
  attr_accessor :value        #읽기 쓰기 모두 가능한 속성으로
  def initialize(v)
    @value = v
  end
  def show()
    p @value
  end
end


c1 = C.new(10)
p c1.value
c1.value = 20
p c1.value
