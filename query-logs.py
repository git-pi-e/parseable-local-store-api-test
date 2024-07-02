import requests
import json

# TODO: Replace the url with your Parseable URL
url = "http://0.0.0.0:8000/api/v1/query"

payload = json.dumps(
    {
        # TODO: Replace the stream name with your log stream name
        "query": "select * from namesdir",
        # TODO: Replace the time range with your desired time range
        "startTime": "2022-09-10T08:20:00+00:00",
        "endTime": "2022-09-10T08:20:31+00:00"
    }
)
headers = {
    # TODO: Replace the basic auth credentials with your Parseable credentials
    "Authorization": "Basic YWRtaW46YWRtaW4=",
    "Content-Type": "application/json",
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
