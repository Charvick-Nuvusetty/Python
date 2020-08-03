import urllib.request
import json

sum=0
url=input('Enter location')
if len(url)<1:
    url= 'http://py4e-data.dr-chuck.net/comments_404509.json'
print('Retrieving' +url)
data=urllib.request.urlopen(url).read()
print('Retrieved',len(data))
info=json.loads(data)
print('User count:',len(info))
for item in info["comments"]:
    num=int(item["count"])
    #print(item['count'])
    sum=sum+num
print(sum)
