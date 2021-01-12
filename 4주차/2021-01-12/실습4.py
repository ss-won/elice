import string

def encode_char(char):
    if char in string.ascii_lowercase:
        return chr(ord('z') - ord(char) + ord('a'))
    if char in string.ascii_uppercase:
        return chr(ord('Z') - ord(char) + ord('A'))
    return char


def decode_char(char):
    if char in string.ascii_lowercase:
        return chr(ord('z') - ord(char) + ord('a'))
    if char in string.ascii_uppercase:
        return chr(ord('Z') - ord(char) + ord('A'))
    return char


def encode(password):
    
    # 문자열을 뒤집습니다.
    reversed_password = password[::-1] # str(reverse(password.split()))
    
    # 각 글자를 암호화하여 이어 붙입니다.
    encoded = "".join([encode_char(ch) for ch in reversed_password])
    # for None in None:
    #     pass
    
    # 맨 끝에 암호화된 문자열의 길이를 붙입니다.
    result = encoded + str(len(password)%10)
    
    return result


def decode(encoded_password):
    
    # 맨 끝에 붙은 수를 제거합니다.
    number_stripped = encoded_password[:-1]
    
    # 각 글자를 복호화하여 이어 붙입니다.
    decoded = "".join([decode_char(ch) for ch in number_stripped])
    # for None in None:
    #     pass
    
    # 문자열을 뒤집습니다.
    result = decoded[::-1] # str(reverse(decoded.split()))
    
    return result


epwd = encode("hello")
dpwd = decode(epwd)
print(epwd, dpwd)