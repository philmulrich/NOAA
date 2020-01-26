import json
import requests
satID=input("NORAD ID: ")
r=requests.get('https://www.n2yo.com/rest/v1/satellite/tle/'+satID+'/&apiKey=YUYMGA-T96SHL-QFVKMQ-4AB5')
print(r.content)


