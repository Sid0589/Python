import requests
import json
import sys

def postToslack(Webhook_url,messageTopost):
    payload = {
        "attachments": [
            {
                "color": "#36a64f",
                "pretext": "",
                "author_name": "Soupam",
                "title": "Testing ",
                "text": "Hello",
                "fields": []
            }
        ]
    }
    if not isinstance(messageTopost,dict):
        exit(2)
    
    payload['attachments'][0]['color'] = messageTopost['color'] if 'color' in messageTopost else '#36a64f'
    payload['attachments'][0]['pretext'] = messageTopost['pretext'] if 'pretext' in messageTopost else ''
    payload['attachments'][0]['author_name'] = messageTopost['author_name'] if 'author_name' in messageTopost else ''
    payload['attachments'][0]['title'] = messageTopost['title'] if 'title' in messageTopost else ''
    payload['attachments'][0]['text']  = messageTopost['text']  if 'text'  in messageTopost else ''
    payload['attachments'][0]['fields'] = []
    if 'fields' in messageTopost:
        for each_row in messageTopost['fields']:
            payload['attachments'][0]['fields'].append(each_row)
    else:
        payload['attachments'][0]['fields'] = []
    for keys in messageTopost:
        if keys not in payload:
            payload[keys] = messageTopost[keys]
    print payload
    try:
        response = requests.post(Webhook_url, data = json.dumps(payload),headers={'Content-Type': 'application/json'})
        if response.status_code !=200:
            print "Could not post to Slack.Following exception occurred - statuscode:-%s,statusmessage-%s" %(response.status_code, response.text)
    except Exception as e:
        print 'The following Exception occurred  - %s ' %str(e.args)
