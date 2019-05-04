import requests, os, json

model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')

url = 'http://app.nanonets.com/api/v2/ImageCategorization/Model/' + model_id

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(api_key,''))

state = json.loads(response.text)["state"]
status = json.loads(response.text)["status"]

if state != 5:
	print "The model isn't ready yet, it's status is:", status
	print "We will send you an email when the model is ready. If your imapatient, run this script again in 10 minutes to check."
else:
	print "NEXT RUN: python ./code/prediction.py ./images/videoplayback0051.jpg"