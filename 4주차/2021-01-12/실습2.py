import string

def validate_name(name):
    
    # name이 문자열인지 확인합니다.
    if not type(name) is str:
        return  False
    
    # name이 숫자를 포함하는지 확인합니다.
    if any([c in name for c in string.digits]):
        return False
    
    # name이 특수기호를 포함하는지 확인합니다.
    if any([c in name for c in string.punctuation]):
        return False
    return True

print(validate_name("asdf2314")) # False

# any() -> list에서 True한 값이 하나라도 있으면 True 아니면 False 반환하는 파이썬 내장 함수
# string.digits = "0123456789"
# string.punctuation = 파이썬에서 기본적으로 입력 가능한 특수문자(,?* 등)을 모아둔 문자열