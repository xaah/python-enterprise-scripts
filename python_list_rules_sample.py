
# Sample Python Script for Listing the Rules in the PowerTrack API (with Python 3)

import base64
import json
import urllib.request
import urllib.parse

# Insert Gnip Console Username and Password Below
UN = ''
PWD = ''

# Insert Your Account Name and Stream Label Into the URL
base_url = 'https://gnip-api.twitter.com/rules/powertrack/accounts/<INSERT_ACCOUNT_NAME_HERE>/publishers/twitter/<INSERT_STREAM_LABEL_HERE>.json'

# Create URL Structure
class RequestWithMethod(urllib.request.Request):
	def __init__(self, base_url, method, headers={}):
		self._method = method
		urllib.request.Request.__init__(self, base_url, headers)
		def get_method(self):
			if self._method:
				return self._method
			else:
				return urllib.request.Request.get_method(self)

# Create Endpoint and Add Credentials
def create_rule_endpoint():
	base64string = ('%s:%s' % (UN, PWD)).replace('\n', '')
	base = base64.b64encode(base64string.encode('ascii'))
	final_url = urllib.request.Request(url=base_url)
	final_url.add_header('Content-type', 'application/json')
	final_url.add_header('Authorization', 'Basic %s' % base.decode('ascii'))
	return final_url

# Take in the Endpoint and Make the HTTP Request
def post_rule(rules_endpoint):
	try:
		response = urllib.request.urlopen(rules_endpoint)
		response_data = response.read()
		print("RESPONSE: %s" % response_data.decode('ascii'))
	except urllib.request.HTTPError as e:
		print("ERROR: %s" % e.decode('ascii'))

# Set the Rule Endpoint to a Variable
post_rules_endpoint = create_rule_endpoint()

# Make the Request by Passing in Rule Endpoint
post_rule(post_rules_endpoint)