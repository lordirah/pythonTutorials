from __future__ import print_function
from requests_oauthlib import OAuth2Session  
import os
import pickle
import json

# Replace with your App's Client ID and Secret
CLIENT_ID     = '116da3f4-fe6d-4c8d-9085-71c4bbdb023d'
CLIENT_SECRET = 'faeaae60-11d3-4af4-b98d-3e28866e9201'

# If modifying these scopes, delete the file hstoken.pickle.
SCOPES        = ['crm.objects.contacts.read']

#================================================================
#==== QuickStart Command-line App

def main():
    """
    Connects your app a Hub, then fetches the first Contact in the CRM.
    Note: If you want to change hubs or scopes, delete the `hstoken.pickle` file and rerun.
    """
    app_config = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scopes': SCOPES,
        'auth_uri': 'https://app.hubspot.com/oauth/authorize',
        'token_uri': 'https://api.hubapi.com/oauth/v1/token'
    }

    # The file hstoken.pickle stores the app's access and refresh tokens for the hub you connect to.
    # It is created automatically when the authorization flow completes for the first time.
    if os.path.exists('hstoken.pickle'):
        with open('hstoken.pickle','rb') as tokenfile:
            token = pickle.load(tokenfile)
    # If no token file is found, let the user log in (and install the app if needed)
    else:
        token = InstallAppAndCreateToken(app_config)
        # Save the token for future runs
        SaveTokenToFile(token)

    # Create an OAuth session using your app_config and token
    hubspot = OAuth2Session(
        app_config['client_id'], 
        token=token, 
        auto_refresh_url=app_config['token_uri'],
        auto_refresh_kwargs=app_config, 
        token_updater=SaveTokenToFile
    )
    print(hubspot.access_token)
    # Call the 'Get all contacts' API endpoint
    from hubspot import HubSpot
    api_client = HubSpot(access_token=hubspot.access_token)
    all_contacts = api_client.crm.contacts.get_all()

    # Pretty-print our API result to console
    #print(all_contacts)

    
#===================================================================
#==== Supporting Functions and Classes used by the command-line app. 

def InstallAppAndCreateToken(config, port=0):
    """
    Creates a simple local web app+server to authorize your app with a HubSpot hub.
    Returns the refresh and access token.
    """  
    from wsgiref import simple_server
    import webbrowser

    local_webapp = SimpleAuthCallbackApp()
    local_webserver = simple_server.make_server(host='localhost', port=port, app=local_webapp)

    redirect_uri = 'http://{}:{}/'.format('localhost', local_webserver.server_port)

    oauth = OAuth2Session(
        client_id=config['client_id'],
        scope=config['scopes'],
        redirect_uri=redirect_uri
    )

    auth_url, _ = oauth.authorization_url(config['auth_uri'])
    
    print('-- Authorizing your app via Browser --')
    print('If your browser does not open automatically, visit this URL:')
    print(auth_url)
    webbrowser.open(auth_url, new=1, autoraise=True)
    local_webserver.handle_request()

    # Https required by requests_oauthlib 
    auth_response = local_webapp.request_uri.replace('http','https')

    token = oauth.fetch_token(
        config['token_uri'],
        authorization_response=auth_response,
        # HubSpot requires you to include the ClientID and ClientSecret
        include_client_id=True,
        client_secret=config['client_secret']
    )
    return token

class SimpleAuthCallbackApp(object):
    """
    Used by our simple server to receive and 
    save the callback data authorization.
    """
    def __init__(self):
        self.request_uri = None
        self._success_message = (
            'All set! Your app is authorized.  ' + 
            'You can close this window now and go back where you started from.'
        )

    def __call__(self, environ, start_response):
        from wsgiref.util import request_uri
        
        start_response('200 OK', [('Content-type', 'text/plain')])
        self.request_uri = request_uri(environ)
        return [self._success_message.encode('utf-8')]

def SaveTokenToFile(token):
    """
    Saves the current token to file for use in future sessions.
    """
    with open('hstoken.pickle', 'wb') as tokenfile:
        pickle.dump(token, tokenfile)
        
if __name__ == '__main__':
    main()