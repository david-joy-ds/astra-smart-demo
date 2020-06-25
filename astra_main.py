from astraconnect import astraConnect as ac
from astra_keyspace import astraKeyspace as ak
from astra_interact import astraInteract as ai
import json
import uuid

# authentication connect
url = "https://cca4ebb0-d9f1-4214-b5ac-53a5532f3b8d-us-east1.apps.astra.datastax.com/api/rest/v1/auth"
headers = {
    'accept': "*/*",
    'x-cassandra-request-id': "X-Cassandra-Request-Id",
    'content-type': "application/json"
    }

auth_token = ac.connect(url,headers)
token = json.loads(auth_token)['authToken']
print(token)

# Extract Keyspaces
keyspace_url =  "https://cca4ebb0-d9f1-4214-b5ac-53a5532f3b8d-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces"
headers1 = {
    'accept': "application/json",
    'x-cassandra-request-id': f"{uuid.uuid4()}",
    'x-cassandra-token': f"{token}",
    'content-type': "application/json"
    }

print(uuid.uuid4())

keyspace = ak.keyspace(keyspace_url,headers1)
print(keyspace)

# Create table 
table_url = keyspace_url+"/dj_keyspace/tables"
print(table_url)

table_response = ak.createTable(table_url,headers1)
print(table_response)

# Use table 
insert_url = keyspace_url+"/dj_keyspace/tables/t1_table/rows"
table_insert = ai.insertTable(insert_url,headers1)
print(table_insert)

#read Table 
read_url = keyspace_url+"/dj_keyspace/tables/twitterdata/rows/bitcoinconnect"
table_read = ai.readTable(read_url,headers1)
print(table_read)


