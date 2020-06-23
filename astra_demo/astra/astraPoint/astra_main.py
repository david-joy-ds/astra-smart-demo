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

        read_url = url+"/keyspaces/dj_keyspace/tables/test_table/rows/1"
        headers1 = {
                    'accept': "application/json",
                    'x-cassandra-request-id': f"{uuid.uuid4()}",
                    'x-cassandra-token': f"{token}",
                    'content-type': "application/json"
                   }

        table_read = ai.readTable(read_url, headers1)
        return {"token":token, "value":table_read};



