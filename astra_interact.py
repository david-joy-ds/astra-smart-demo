import requests

class astraInteract:

    def insertTable(insert_url, headers1) : 
        payload = '{"columns":[{"name":"rowid","value":2}, {"name":"rowvalue", "value":"entry 2"}]}'
        response = requests.request("POST", insert_url, headers=headers1, data=payload)
        return response.text ; 

    def readTable(read_url,headers1):
        response = requests.request("GET", read_url, headers=headers1)
        return response.text ;
