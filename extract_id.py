import json
try:
    d = json.load(open('google-services.json'))
    clients = d.get('client', [{}])[0].get('oauth_client', [])
    web_id = next((c['client_id'] for c in clients if c['client_type'] == 3), 'NOT_FOUND')
    print(web_id)
except Exception as e:
    print('NOT_FOUND')
