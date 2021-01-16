import re

emails = ["abc@elice.com", "a1b2c3@daum.net",
          "!&(*@&#!)@elice.co.kr", "hello", "isThisEmail?",
          "john.kim@elice.com", "john.kim12@elice.com", "a@elice.com"]

p = re.compile("[\w]*[.]?[\w]+@[\w][.]?[\w]+")
for email in emails:
    m = p.match(email)
    if m is not None:
        print(m.group())
