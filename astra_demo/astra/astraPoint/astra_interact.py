import requests

class astraInteract:

    def insertTable(insert_url, headers1,payload) :
        for i in range(0,len(payload)):
            response = requests.request("POST", insert_url, headers=headers1, data=payload[i])

        return response.text;

    def readTable(read_url, headers1):
        response = requests.request("GET", read_url, headers=headers1)
        return response.text;