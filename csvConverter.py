import csv, json

fileAddress = 'ip.csv'


def getDataListFromCSV(fileAddress):
    pack = []
    with open(fileAddress, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            pack.append(row)
        return pack


def getDictFromListSortByTitle(column, dataList):
    d1, d2 = {}, {}
    for j in range(len(dataList)):
        i = 0
        for x in dataList[j]:
            d1[column[i]], d2[j] = x, d1
            i += 1
    return d2

pack = getDataListFromCSV(fileAddress)
titles = pack[0]
pack.remove(pack[0])
dx = getDictFromListSortByTitle(titles, pack)
print(json.dumps(dx, ensure_ascii=False))
