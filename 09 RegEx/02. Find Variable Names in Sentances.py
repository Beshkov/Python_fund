import re

data = input()

pattern = r"(?<= _)[A-Za-z0-9]+\b"

re_match = re.findall(pattern, data)

print(",".join(re_match))