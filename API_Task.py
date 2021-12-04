from urllib.request import urlopen
from json import loads
from itertools import groupby

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE%2C_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))
sortedData = list()
for key, group in groupby(data['query']['pages']['192203']['revisions'], lambda x: x['timestamp'][:10]):
    sortedData.append(key + ' ' + len(list(group)).__str__())
sortedData.sort(key=lambda x: int(x.split(' ')[1]))
for obj in reversed(sortedData):
    print(obj)
