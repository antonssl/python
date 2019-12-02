import boto3
import requests
from datetime import date, timedelta, datetime

s3_client = boto3.client('s3')
api_key = 'xxxxxxxxxx'
headers = 'true'
today = date.today()
job_name = "Data_" + str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
end = today.strftime("%Y-%m-%d")
start = today - timedelta(1)
start = start.strftime("%Y-%m-%d")

url = 'http://www.apiprovider.com/services/ext/export/count?cid=1234&key={}&start={}&end={}&type=hour&objectType=store'.format(
    api_key, start, end, headers)

response = requests.get(url, verify=False)

if response.status_code == 200:
    print("Fetching data from API")
    bucket = 'mytestbucket'
    final_object = 'Incoming_Feeds/' + job_name + '.csv'
    s3_client.put_object(Bucket=bucket, Key=final_object, Body=response.text)

else:
    print("The URL is unresponsive")
