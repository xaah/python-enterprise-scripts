
# Sample Python Script for Deleting a Rule in the PowerTrack API (with Python 3)

import base64
import json
import urllib.request
import urllib.parse

# Insert Gnip Console Username and Password Below
UN = ''
PWD = ''

# Insert Your Account Name and Stream Label Into the URL
base_url = 'https://gnip-api.twitter.com/rules/powertrack/accounts/<INSERT_ACCOUNT_NAME_HERE>/publishers/twitter/<INSERT_STREAM_LABEL_HERE>.json?_method=delete'

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

def delete_rule():
	try:
		delete_rules = ({'rules':[{'value':'testrule'}]})
		encoded_query = json.dumps(delete_rules).encode('ascii')

		base64string = ('%s:%s' % (UN, PWD)).replace('\n', '')
		baseauth = base64.b64encode(base64string.encode('ascii'))

		# Format the request url and add basic authorization
		final_url = urllib.request.Request(base_url)
		final_url.add_header('Authorization', 'Basic %s' % baseauth.decode('ascii'))
		response = urllib.request.urlopen(final_url, encoded_query)
		response_data = response.read()
		print(response_data)
	
	except urllib.request.HTTPError as e:
		print(e.read())

# Make the Request by Passing in Rule Endpoint
delete_rule()
