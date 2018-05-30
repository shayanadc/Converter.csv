import csv,json
pack = []
with open('ip.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
            pack.append(row)
titles = pack[0]
pack.remove(pack[0])
d1 = {}
d2 = {}
for index in range(len(pack)):
    i = 0
    for x in pack[index]:
        # print(index,titles[i],x)
        d1[titles[i]] = x
        # d[index][titles] = d[index][titles[i]][x]
        d2[index] = d1
        i = i+1
# print(json.dumps(d2))
print(json.dumps(d2, ensure_ascii=False))