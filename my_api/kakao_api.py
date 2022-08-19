import requests

def search_api(url, AUTHORIZATION, params) :
    headers = {
        "Authorization" : AUTHORIZATION
    }

    res = requests.get(url, params = params, headers = headers)
    result = res.json()

    if res.status_code != 200 :
        print(result)
        result = None
    
    return result
