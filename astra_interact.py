import requests

class astraInteract:

    def insertTable(insert_url, headers1) :
        payload = '{"columns":[{"name":"rowid","value":"e9b6c02d-0604-4bab-a3ea-6a7984654631"},{"name":"author","value":"Heavy Lift Arms"}]}'
        response = requests.request("POST", insert_url, headers=headers1, data=payload)
        return response.text;

    def readTable(read_url,headers1):
        response = requests.request("GET", read_url, headers=headers1)
        return response.text ;
