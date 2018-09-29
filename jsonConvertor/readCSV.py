import csv, json

fileAddress = 'test.csv'


def getDataListFromCSV(fileAddress):
    pack = []
    with open(fileAddress, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            pack.append(row)
        return pack


def bindListByTitle(column, dataList):
    d1, d2 = {}, {}
    for j in range(len(dataList)):
        i = 0
        for x in dataList[j]:
            d1[column[i]], d2[j] = x, d1
            i += 1
    return d2
def convertCSVFiletoJson(fileAddress):
    pack = getDataListFromCSV(fileAddress)
    titles = pack[0]
    pack.remove(pack[0])
    list = bindListByTitle(titles, pack)
    return json.dumps(list, ensure_ascii=False)

print(convertCSVFiletoJson(fileAddress))