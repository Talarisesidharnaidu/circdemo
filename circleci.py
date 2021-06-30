#import http.client
#conn = http.client.HTTPSConnection("circleci.com")
#headers = { 'authorization': "Basic 3e9d9cad13f63c7ee27967b1894b08bd7738aecd" }
#conn.request("GET", "https://app.circleci.com/pipelines/github/Talarisesidharnaidu/circdemo/", headers=headers)
#res = conn.getresponse()
#print(res.status)
#print(data)
#print(data.decode("utf-8"))

#conn.request("GET", "/api/v2/project/gh/CircleCI-Public/api-preview-docs/job/1000", headers=headers)



import http.client

conn = http.client.HTTPSConnection("circleci.com")

headers = { 'authorization': "Basic 3e9d9cad13f63c7ee27967b1894b08bd7738aecd" }

conn.request("GET", "/api/v2/project/gh/Talarisesidharnaidu/circdemo/workflow/build_and_test/job", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))