import requests, json, subprocess

authorize_url = "https://app.hubspot.com/oauth/authorize"
token_url = "https://api.hubapi.com/oauth/v1/token"

#callback URL specified when the application was defined
callback_uri = "http://localhost:8083/oauth_redirect"

test_api_url = "https://api.hubapi.com/crm/v3/objects/contacts"

#client (application) credentials on apim.byu.edu
client_id = '116da3f4-fe6d-4c8d-9085-71c4bbdb023d'
client_secret = 'faeaae60-11d3-4af4-b98d-3e28866e9201'


#step A - single call with client id and call back url on the url
# will return access_token
authorization_redirect_url = 'https://app.hubspot.com/oauth/authorize?client_id=116da3f4-fe6d-4c8d-9085-71c4bbdb023d&redirect_uri=http%3A%2F%2Flocalhost%3A8083%2Foauth_redirect&scope=crm.objects.contacts.read&optional_scope=&state='


print("go to the following url on the browser and enter the code from the returned url: ")
print("---  " + authorization_redirect_url + "  ---")
access_token = input('access_token: ')

#step H - we can now use the returned access_token to 

api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

print(api_call_response.text)