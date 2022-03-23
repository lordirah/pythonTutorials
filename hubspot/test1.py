from hubspot.auth.oauth import ApiException
from hubspot import HubSpot

#api_client = HubSpot()

# tokens = api_client.auth.oauth.default_api.create_token(
#         grant_type="authorization_code",
#         redirect_uri='http://localhost:8083/oauth_redirect',
#         client_id='116da3f4-fe6d-4c8d-9085-71c4bbdb023d',
#         client_secret='faeaae60-11d3-4af4-b98d-3e28866e9201',
#         code='eu1-9240-c526-4038-82ad-d24286f7d335'
#     )

# print(tokens)
from hubspot.utils.oauth import get_auth_url

auth_url = get_auth_url(
    scopes=('crm.objects.contacts.read',),
    client_id='116da3f4-fe6d-4c8d-9085-71c4bbdb023d',
    redirect_uri='http://localhost:8080/'
)

print(auth_url)