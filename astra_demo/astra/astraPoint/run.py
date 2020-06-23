from astra_main import connect

url = "https://cca4ebb0-d9f1-4214-b5ac-53a5532f3b8d-us-east1.apps.astra.datastax.com/api/rest/v1"
post = connect.connection(url)
print(post)