import requests

def search_api(url, Authorization, params) :
    headers = {
        "Authorization" : Authorization
    }

    res = requests.get(url, params = params, headers = headers)
    result = res.json()

    if res.status_code != 200 :
        print(result)
        result = None
    
    return result
