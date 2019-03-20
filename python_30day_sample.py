
# Sample Python Script for Searching with the 30-Day Search API (with Python 3)

import base64
import json
import urllib.request
import urllib.parse

# Insert Gnip Console Username and Password Below
UN = ''
PWD = ''

# Insert Your Account Name and Stream Label Into the URL
base_url = 'https://gnip-api.twitter.com/search/30day/accounts/<INSERT_ACCOUNT_NAME_HERE>/<INSERT_STREAM_LABEL_HERE>.json?query='

# Create URL Structure
class RequestWithMethod(urllib.request.Request):
	def __init__(self, base_url, method, headers={}):
		self._method = method
		urllib.request.Request.__init__(self, base_url, headers)
	def post_method(self):
		if self._method:
			return self._method
		else:
			return urllib.request.Request.post_method(self)

#Create Endpoint & Add Credentials
def create_url(query):
		base64string = ('%s:%s' % (UN, PWD)).replace('\n', '')
		base = base64.b64encode(base64string.encode('ascii'))
		encoded_query = urllib.parse.urlencode({'query' : '{query}'})
		new_url = base_url + encoded_query
		final_final_url = urllib.request.Request(new_url)
		final_final_url.add_header('Authorization', 'Basic %s' % base.decode('ascii'))
		return final_final_url

# Take in the Endpoint and Make the Request
def make_request(search_endpoint):
	try:
		response = urllib.request.urlopen(search_endpoint)
		response_data = response.read()
		handle_response(response_data)
	except urllib.request.HTTPError as error:
		print("ERROR: %s" % error)

# Handle the Returned Data and Print Tweet Text
def handle_response(data):
	tweets_returned = json.loads(data)
	for tweet in tweets_returned['results']:
		tweet_text = tweet['text']
		print("TWEET_TEXT:  %s:" % tweet_text)

# Create the Endpoint Variable w/ Sample Query
search_endpoint = create_url('(coffee OR Tea) (pizza OR bagel)')

# Make the Request by Passing in Search Endpoint
make_request(search_endpoint)
