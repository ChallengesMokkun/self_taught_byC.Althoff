import re

line = "I love $"
m = re.findall("\$",line)
print(m)
