import re

text = "my name is lucifer"
match = re.search("lucifer", text)
print("Search found:", match.group() if match else "Not found")

match = re.match("paras", text)
print("Match found:", match.group() if match else "Not found")