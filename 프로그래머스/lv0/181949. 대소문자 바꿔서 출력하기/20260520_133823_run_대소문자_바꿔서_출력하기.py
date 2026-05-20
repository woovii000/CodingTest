str = input()
for c in str:
    if c.isupper():
        c.lower()
    else:
        c.upper()
print(str)