import http.client

conn = http.client.HTTPSConnection("circleci.com")

headers = { 'authorization': "Basic 3e9d9cad13f63c7ee27967b1894b08bd7738aecd" }

conn.request("GET", "/api/v2/project/gh/Talarisesidharnaidu/circdemo/pipeline?branch=main&page-token=Basic 3e9d9cad13f63c7ee27967b1894b08bd7738aecd", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))