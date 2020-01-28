import time
from datetime import datetime
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
#passResponse=r.content
#print(passResponse)
#print('\n\n')
x=r.json()

startUTC=(x['passes'][0]['startUTC'])
startUTC=int(startUTC)
endUTC=(x['passes'][0]['endUTC'])
endUTC=int(endUTC)
nowUTC=time.time()
nowUTC=int(nowUTC)
sleepTime=startUTC-nowUTC
recordTime=endUTC-startUTC
print(sleepTime)
print(recordTime)

#theoratically
#time.sleep(sleepTime)
#os.system('Record for {recordTime} -o audio.wav' -f 137100)
#os.system('noaa-apt audio.wav -r 11025 -o audio.wav')
#os.system('noaa-apt audio.wav -o photo')
#upload photo to website
#REPEAT ENTIRE PROCESS
