import requests

class astraConnect:

    def connect(url,headers) : 
        data = '{"username":"'"david"'", "password":"'"qwerty"'"}'
        response = requests.request("POST", url, headers=headers, data=data)
        return response.text ;