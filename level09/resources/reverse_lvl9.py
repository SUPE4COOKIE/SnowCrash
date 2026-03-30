with open("token", "rb") as f:
    token = f.read().strip()

result = ""
for i, b in enumerate(token):
    result += chr(ord(b) - i)
print(result)