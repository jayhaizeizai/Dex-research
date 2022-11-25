import requests
import json
import datetime
import time

params = {
    'symbol': 'BTCUSDC',
}

ISOTimeFormat = '%Y-%m-%d %H:%M:%S'
i=0
while True:
    theTime= datetime.datetime.now()

    response = requests.get('https://pro.apex.exchange/api/v1/ticker', params=params)
    json1=json.loads(response.text)
    #print(json.dumps(json1, indent=4, sort_keys=True))
    data=json1["data"]
    #print(data)
    data_dict=data[0]
    #print(type(data_dict["lastPrice"]))
    lastPrice=float(data_dict["lastPrice"])
    #print(lastPrice)

    #print(type(data_dict["oraclePrice"]))
    oraclePrice=float(data_dict["oraclePrice"])
    #print(oraclePrice)
    Diff_ratio=lastPrice/oraclePrice
    if (Diff_ratio<0.998)or(Diff_ratio>1.002):
        print('Here')
        print("Diff_ratio=" + str(Diff_ratio) + ' @ ' + str(theTime))
    i=i+1
    if(i%12==0):
        print('Current running time is '+str(i/12)+'minutes')
    time.sleep(5)


