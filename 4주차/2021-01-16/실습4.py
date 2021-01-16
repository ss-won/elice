import re

# 1. Regular expression
p = re.compile("[a-z]+")
m = p.match("elice")

print(m.group())
print(m.start())
print(m.end())
print(m.span())

# 2. phone_numbers validation
# phone_numbers = ["010-1234-1234", "0101234123",
#                  "010-12341234", "017-123-1234",
#                  "016-1231234", "010-123-1234",
#                  "+82-1234-1234"]

# p = re.compile("([0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4})")
# # p = re.compile("(\d{3}[-]?\d{4}[-]?\d{4})")
# for number in phone_numbers:
#     m = p.match(number)
#     if m is not None:
#         print(m)
