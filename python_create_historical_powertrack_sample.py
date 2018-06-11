
# Sample Python Script for Creating a New Job with the Historical PowerTrack Search API (with Python 3)

import base64
import json
import urllib.request
import urllib.parse

# Insert Gnip Console Username and Password Below
UN = ''
PWD = ''

# Insert Your Account Name and Stream Label Into the URL
base_url = 'https://gnip-api.gnip.com/historical/powertrack/accounts/<INSERT_ACCOUNT_NAME_HERE>/publishers/twitter/jobs.json'
headers = {"publisher":"Twitter","dataFormat":"activity_streams","fromDate":"201301010000","toDate":"201301010001","title":"my_job12","rules":[{"value":"dogs are cool"}]}

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

#Create Endpoint & Add Credentials
def create_rules_endpoint():
    print("HEADERS:  %s:" % headers)
    base64string = ('%s:%s' % (UN, PWD)).replace('\n', '')
    base = base64.b64encode(base64string.encode('ascii'))
    data = bytes(json.dumps(headers), encoding='ascii')
    final_url = urllib.request.Request(url=base_url, data=data)
    final_url.add_header('Authorization', 'Basic %s' % base.decode('ascii'))   
    return final_url

#Take in the Endpoint and Make the Request
def make_request(search_endpoint):
    try:
        response = urllib.request.urlopen(search_endpoint)
        response_data = response.read()
        print("RESPONSE:  %s:" % response_data)
    except urllib.request.HTTPError as error:
        print("ERROR: %s" % error)

# Create the Endpoint Variable w/ Sample Query Keyword
search_endpoint = create_rules_endpoint()

# Make the Request by Passing in Search Endpoint
make_request(search_endpoint)