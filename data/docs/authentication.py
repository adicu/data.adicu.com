lead =  """To use any of the API's you must have an api_token
        and appended to your string as api_token=TOKEN. To get a
        token, login on the upper right. We use google auth to make
        the auth request. Once signed in, visit the token page to see
        your token, and get coding!"""

endpoints =  None

def get_lead():
    return lead

def get_endpoints():
    return endpoints
