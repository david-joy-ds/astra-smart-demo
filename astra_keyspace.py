import requests

class astraKeyspace:

    def keyspace(kurl, headers1) : 
        response = requests.request("GET", kurl, headers=headers1)
        return response.text ;

    
    def createTable(table_url, headers1) : 
        data = '{"name":"products","ifNotExists":true, "columnDefinitions":[ {"name":"id","typeDefinition":"uuid","static":false}, {"name":"name","typeDefinition":"text","static":false}, {"name":"description","typeDefinition":"text","static":false}, {"name":"price","typeDefinition":"decimal","static":false}, \
  {"name":"created","typeDefinition":"timestamp","static":false}],"primaryKey": {"partitionKey":["id"]},"tableOptions":{"defaultTimeToLive":0}}'
        response = requests.request("POST", table_url, headers=headers1, data=data)
        return response.text ; 