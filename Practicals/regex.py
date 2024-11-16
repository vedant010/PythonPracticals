import re

text = "Hello world!"
match = re.match(r"Hello", text) 
if match:
    print("Found:", match.group())
else:
    print("No match")

search = re.search(r"world", text)  
if search:
    print("Found:", search.group())
else:
    print("No match")

numbers = re.findall(r"\d+", "phone number is 12345 and zip code is 67890")
print("Found numbers:", numbers)

modified_text = re.sub(r"\d", "X", "My phone number is 12345")
print("Modified text:", modified_text)
