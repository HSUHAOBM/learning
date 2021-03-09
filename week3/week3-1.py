import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"

with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["results"]    
# for APIdata in clist:
#     print(APIdata["stitle"]+","+APIdata["longitude"]+","+APIdata["latitude"]+",http://"+APIdata["file"].split("http://")[1])
with open("data.txt","w",encoding="utf-8") as file:
    for APIdata in clist:
        file.write(APIdata["stitle"]+","+APIdata["longitude"]+","+APIdata["latitude"]+",http://"+APIdata["file"].split("http://")[1]+"\n")
# print(clist)