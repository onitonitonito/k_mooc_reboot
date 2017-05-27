import keyword, random

def kw_show():
    print(keyword.kwlist)
#kw_show()

first = []
print(first)

for x in range(10):
    first.append(random.randint(0,11))
print(first)

first = []
print(first)

first = [random.randint(0,11) for x in range(10)]
print(first)

name = ["aura", "proxy", "kira",]
role = ["medic", "engineer", "firesupport"]
lvl = [56, 72, 61,]

DBnation_team = {name: [role, lvl] for name, role, lvl in zip(name, role, lvl)}
print (DBnation_team)

print(DBnation_team["proxy"][0])
