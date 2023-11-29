import re

str = "i am blogger at https://www.google.com/"

url = re.findall(str)
print(url)


