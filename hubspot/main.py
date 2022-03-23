from flask import Blueprint, render_template
from flask import request, redirect
import json
from .oauth_form import OauthForm
import urllib.parse

import traceback

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/hubspot_oauth')
def hubspot_oauth():
    CLIENT_ID = urllib.parse.quote_plus(YOURCLIENTID)
    REDIRECT_URI = urllib.parse.quote_plus("http://localhost:8083/oauth_redirect")
    SCOPES = urllib.parse.quote_plus("contacts content reports social automation transactional-email integration-sync tickets e-commerce crm.objects.marketing_events.read crm.schemas.custom.read crm.objects.custom.read sales-email-read forms-uploaded-files")

    auth_url = """https://app.hubspot.com/oauth/authorize?client_id=%s&scope=%s&redirect_uri=%s"""%(CLIENT_ID, SCOPES, REDIRECT_URI)

    return redirect(auth_url, code=302)

@home_blueprint.route('/oauth_redirect')
def hubspot_oauth_redirect():
    code = request.args.get("code")

    form = OauthForm()
    form.code.data = code

    url = "https://api.hubapi.com/oauth/v1/token"
    ClientID = 'YOURCLIENTID'
    ClientSecret = 'YOURCLIENTSECRET'
    REDIRECT_URI = 'http://localhost:8083/oauth_redirect' # same URL as above
    formData = {
        "grant_type": 'authorization_code',
        "client_id": ClientID,
        "client_secret": ClientSecret,
        "redirect_uri": REDIRECT_URI,
        "code": code
    }

    data = urllib.parse.urlencode(formData)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, method='POST')
    access_token = None
    refresh_token = None

    with urllib.request.urlopen(req) as response:
        data = None
        try:
            data = response.read()
            parsed_data = json.loads(data)
            access_token = parsed_data.get("access_token")
            refresh_token = parsed_data.get("refresh_token")
        except:
            traceback.print_exc()

    form.access_token.data = access_token
    form.refresh_token.data = refresh_token


    return render_template('oauth.html', form=form)