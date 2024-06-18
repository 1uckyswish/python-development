session = []

session.append(1)
session.append(2)
session.append(3)

print(session)
last = session.pop()
print(last)
print(session)

print("last", session[-1])

if not session:
    print("disable")