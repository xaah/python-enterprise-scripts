
# Sample Python Script for Creating a New Rule in the PowerTrack API (with Python 3)

import base64
import json
import urllib.request
import urllib.parse

# Insert Gnip Console Username and Password Below
UN = ''
PWD = ''

# Insert Your Account Name and Stream Label Into the URL
base_url = 'https://gnip-api.twitter.com/rules/powertrack/accounts/<INSERT_ACCOUNT_NAME_HERE>/publishers/twitter/<INSERT_STREAM_LABEL_HERE>.json?rule='

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

# Create Endpoint and Add Credentials
def create_rule_endpoint(rule):
	# Create sample rule with rule tag
	base64string = ('%s:%s' % (UN, PWD)).replace('\n', '')
	base = base64.b64encode(base64string.encode('ascii'))
	encoded_query = urllib.parse.urlencode({'value' : rule})
	new_url = base_url + encoded_query
	final_url = urllib.request.Request(new_url)
	final_url.add_header('Authorization', 'Basic %s' % base.decode('ascii'))
	return final_url

# Take in the Endpoint and Make the Request
def post_rule(rules_endpoint):
	try:
		response = urllib.request.urlopen(rules_endpoint)
		response_data = response.read()
		print("RESPONSE: %s" % response_data.decode('UTF-8'))
	except urllib.request.HTTPError as e:
		print(e)

# Set the Rule Endpoint to a Variable
post_rules_endpoint = create_rule_endpoint('(sports OR news OR technology) today')

# Make the Request by Passing in Rule Endpoint
post_rule(post_rules_endpoint)
