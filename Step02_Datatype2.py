# 특정 시점에 실행할 코드 블럭을 함수에 모아 놓을 수 있다.

def store():
    print("냉장고 문을 연다")
    print("음식을 저장한다")
    print("냉장고 문을 닫는다")


store()

#함수에 리턴하는 값을 변수에 담아보면?
result = store() # None 이 result 에 들어간다

# 변수를 미리 만들어 두고 값을 나중에 넣고 싶으면 None 을 대입해서 변수를 만들면 된다.
print("Step02_Datatype2.py가 종료 됩니다.")