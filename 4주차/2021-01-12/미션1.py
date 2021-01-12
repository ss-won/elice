import string

def validate_password(password):

    # 문자열이 8자 이상인지 확인합니다.
    is_long = False
    if len(password) >= 8:
        is_long = True
    
    # 문자열에 숫자가 포함되어 있는지 확인합니다.
    includes_digit = False
    for digit in password:
        if digit in string.digits:
            includes_digit = True
            break
    
    # 문자열에 알파벳 대문자가 포함되어 있는지 확인합니다.
    includes_upper = False
    for char in password:
        if char in string.ascii_uppercase:
            includes_upper = True
            break
    
    # 문자열에 알파벳 소문자가 포함되어 있는지 확인합니다.
    includes_lower = False
    for char in password:
        if char in string.ascii_lowercase:
            includes_lower = True
            break
    
    return is_long and includes_digit and includes_upper and includes_lower


def validate_birthday(birthday):
    
    year, month, day = birthday
    
    # 연도가 조건에 맞는지 확인하고, 아니면 False를 return 합니다.
    if not(year >= 1900 and year <= 2018):
        return False
    
    # 달이 31일까지 있는 경우, 날짜가 유효한지 체크합니다.
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not(day >= 1 and day <= 31):
            return False
    
    # 달이 30일까지 있는 경우, 날짜가 유효한지 체크합니다.
    elif month in [4, 6, 9, 11]:
        if not(day >= 1 and day <= 30):
            return False
    
    # 2월인 경우, 날짜가 유효한지 체크합니다.
    else:
        if is_leap_year(year):
            if not(day >= 1 and day <= 29):
                return False
        else:
            if not(day >=1 and day <= 28):
                return False
    

# 윤년 계산
def is_leap_year(year):
    
    # 조건 1
    if year%4 != 0:
        return False
    
    # 조건 2
    elif year%100 != 0:
        return True
    
    # 조건 3
    elif year%400 == 0:
        return True
    
    # 모두 아닌 경우
    else:
        return False


# 여러분의 코드를 직접 테스트해 보세요.
is_password_valid = validate_password("qwRrty!3")
print(is_password_valid)

is_birthday_valid = validate_birthday((1988, 2, 30))
print(is_birthday_valid)

is_2000_leap = is_leap_year(2000)
print(is_2000_leap)
