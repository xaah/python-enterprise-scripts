
# Sample Python Script for Connecting to the PowerTrack Streaming (with Python 3)

import urllib.request
import urllib.parse
import base64
import zlib
import json
import sys
import ssl
import certifi
import csv

# Set Chunksize, Keepalive, and Newlines Below
CHUNKSIZE = 4*1024
GNIPKEEPALIVE = 30  # seconds
NEWLINE = '\r\n'

# Insert Gnip Console Username and Password Below
UN = ''
PWD = ''

# Insert Your Account Name and Stream Label Into the URL
URL = 'https://gnip-stream.twitter.com/stream/powertrack/accounts/<INSERT_ACCOUNT_NAME_HERE>/publishers/twitter/<INSERT_STREAM_LABEL_HERE>.json'
HEADERS = { 'Accept': 'application/json',
            'Connection': 'Keep-Alive',
            'Accept-Encoding' : 'gzip',
            'Authorization' : (('%s:%s' % (UN, PWD)).replace('\n', '')).encode()
            }

# Create Endpoint, Add Credentials, and Connect to the Stream
def getStream():
    base64string = ('%s:%s' % (UN, PWD)).replace('\n', '')
    base = base64.b64encode(base64string.encode('ascii'))
    final_url = urllib.request.Request(url=URL, headers=HEADERS)
    final_url.add_header('Authorization', 'Basic %s' % base.decode('ascii'))   
    response = urllib.request.urlopen(final_url, timeout=(1+GNIPKEEPALIVE))
    
    # header -  print response.info()
    decompressor = zlib.decompressobj(16+zlib.MAX_WBITS)
    remainder = ''
    while True:
        tmp = decompressor.decompress(response.read(CHUNKSIZE))
        if tmp == '':
            return
        processData(tmp)

# Process and print the data returned to you via the getStream function
def processData(data):
    for rec in [x.strip() for x in data.splitlines(keepends=False) if x.strip() != '']:
        try:
            with open("TweetsFromPowerTrack.csv", "a") as file:
                    json_data = json.dumps([rec.decode()])
                    data = json.loads(json_data)
                    writer = csv.writer(file)
                    writer.writerow(data)
            file.close()
            print(rec.decode())
        except ValueError:
            sys.stderr.write("Error processing JSON: %s (%s)\n"%(str(ValueError), rec))
    

if __name__ == "__main__":
    while True:
        try:
            getStream()
            with err_lock:
                sys.stderr.write("Forced disconnect: %s\n"%(str(e)))
        except ssl.SSLError as e:
            with err_lock:
                sys.stderr.write("Connection failed: %s\n"%(str(e)))
    
