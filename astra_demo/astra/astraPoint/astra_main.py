from astra.astraPoint.astraconnect import astraConnect as ac
from astra.astraPoint.astra_interact import astraInteract as ai
import json
import uuid

class connect() :

    def connection(url):
        # authentication connect
        auth_url = url+"/auth"
        headers = {
            'accept': "*/*",
            'x-cassandra-request-id': f"{uuid.uuid4()}",
            'content-type': "application/json"
        }
        auth_token = ac.connect(auth_url,headers)
        token = json.loads(auth_token)['authToken']

        headers1 = {
        'accept': "application/json",
        'x-cassandra-request-id': f"{uuid.uuid4()}",
        'x-cassandra-token': f"{token}",
        'content-type': "application/json"
        }

        return headers1;


    def read(url,c):
        headers1 = connect.connection(url)
        read_url = url+"/keyspaces/dj_keyspace/tables/twitterdata/rows/"+c
        print(read_url)
        table_read = ai.readTable(read_url, headers1)
        return table_read

    def insert(url, payload):
        headers1 = connect.connection(url)
        insert_url = url+"/keyspaces/dj_keyspace/tables/twitterdata/rows"
        table_insert = ai.insertTable(insert_url, headers1, payload=payload)
        return table_insert;


