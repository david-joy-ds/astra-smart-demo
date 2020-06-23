import requests

class astraKeyspace:

    def keyspace(kurl, headers1) : 
        response = requests.request("GET", kurl, headers=headers1)
        return response.text ;

    
    def createTable(table_url, headers1) : 
        data = '{"name":"test_table", \
                "ifNotExists":true, \
                "columnDefinitions": \
                    [{"name":"rowid","typeDefinition":"int"}, \
                     {"name":"rowvalue","typeDefinition":"text"}], \
                "primaryKey": {"partitionKey":["rowid"]}}'
        response = requests.request("POST", table_url, headers=headers1, data=data)
        return response.text ; 