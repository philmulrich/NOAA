import json
import requests
satID=input("NORAD ID: ")
apiKey='&apiKey=YUYMGA-T96SHL-QFVKMQ-4AB5'
tle = 'https://www.n2yo.com/rest/v1/satellite/tle/'
radioPasses = 'https://www.n2yo.com/rest/v1/satellite/radiopasses/'
coords = '/38.762280/-104.834110/1968/'
days=input("Prediction out to how many days: ")
minAlt=input("Minimum MaxAltitude in Degrees: ")
r=requests.get(tle+satID+apiKey)
tleResponse=r.content
r=requests.get(radioPasses+satID+coords+days+'/'+minAlt+'/'+apiKey)
passResponse=r.content
print(passResponse)



