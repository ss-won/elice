def validate_email(email):
    
    # 주소가 문자열인지 확인합니다.
    if not type(email) is str:
        return False
    
    # 주소가 하나의 @을 포함하는지 확인합니다.
    if email.count('@') != 1:
        return False
        
    # 주소에서 도메인을 추출합니다.
    domain = email.split('@')[-1]
    
    # 도메인이 하나 이상의 점을 포함하는지 확인합니다.
    if domain.count('.') != 1:
        return False
    
    # 도메인을 점 기준으로 쪼개고, 연속하는 점이 없는지 확인합니다.
    # 아래의 코드는 완성되어 있습니다. 코드를 이해해 보세요.
    parts = domain.split(".")
    for part in parts:
        if part == "":
            return False
    
    return True

print(validate_email("asfasdf@asdf.com"))

# string.count(str) = string에서 str이 있는 만큼 counting해주는 문자열 객체 메소드
