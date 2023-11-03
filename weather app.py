import json
import pandas as pd
import requests
import datetime
def get_temperature_variance(city,start_date,end_date):
    URL = 'https://api.oikolab.com/weather'
    OIKO_KEY = '3e45b024800b49c9b0630b0dca2095ec'
    resp=requests.get(URL,
                      params = {
                          'param':['temperature'],
                          'start' :start_date,
                          'location': city,
                          'end' :end_date,
                          'api-key': OIKO_KEY,
                          'freq': 'D'}
    )
    weather_data =resp.json()['data']
    weather_data = json.loads(weather_data)
    df=pd.DataFrame(index=pd.to_datetime(weather_data['index' ], unit='s'),data=weather_data['data'],
            columns=weather_data['columns'])
    variance=df['temperature (degC)'].var()
    return variance
city1=input()
city2 = input()
start_date = input()
start_date = start_date.split('-')
obj1 = datetime.datetime(int(start_date[0]), int(start_date[1]),int(start_date [2]))
obj2= obj1+datetime.timedelta(days=7)
start_date = obj1.strftime('%Y-%m-%d')
end_date = obj2.strftime('%Y-%m-%d')
var1 = get_temperature_variance (city1, start_date, end_date)
var2 = get_temperature_variance(city2, start_date, end_date)
if var1 < var2:
    print (f"We choose {city1} because of less temperature variance")
else:
    print (f"We choose {city2} because of less temperature variance")