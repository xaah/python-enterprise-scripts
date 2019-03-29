# Sample Python Script for Creating a New Job with the Historical PowerTrack Search API (with Python 3)

import base64
import json
import urllib.request
import urllib.parse

# Insert Gnip Console Username and Password Below
UN = ''
PWD = ''

# Insert Your Account Name and Stream Label Into the URL
base_url = 'https://gnip-api.gnip.com/historical/powertrack/accounts/<INSERT_ACCOUNT_NAME_HERE>/publishers/twitter/jobs/<JOB_UUID>.json'

# Create URL Structure
class RequestWithMethod(urllib.request.Request):
    def __init__(self, base_url, method, headers={}):
        self._method = method
        urllib.request.Request.__init__(self, base_url)
    def get_method(self):
        if self._method:
            return self._method
        else:
            return urllib.request.Request.get_method(self)

# Create Endpoint & Add Credentials
def accept_job_endpoint():
    base64string = ('%s:%s' % (UN, PWD)).replace('\n', '')
    base = base64.b64encode(base64string.encode('ascii'))
    final_url = urllib.request.Request(url=base_url)
    final_url.add_header('Authorization', 'Basic %s' % base.decode('ascii'))   
    return final_url

# Create the Endpoint
job_endpoint = accept_job_endpoint()

# Take in the Endpoint and Make the Request
def make_request(job_endpoint):
    try:
        response = urllib.request.urlopen(job_endpoint)
        response_data = response.read()
        print("RESPONSE:  %s:" % response_data)
    except urllib.request.HTTPError as error:
        print("ERROR: %s" % error)

# Make the Request
make_request(job_endpoint)
