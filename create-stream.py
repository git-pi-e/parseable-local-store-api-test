import requests
from requests.auth import HTTPBasicAuth

# Replace the URL with your Parseable URL and stream name
url = "http://0.0.0.0:8000/api/v1/logstream/namesdir"
payload = {}

# Basic Authentication credentials
username = "admin"
password = "admin"

# Headers
headers = {
    "Content-Type": "application/json"
}

try:
    # Make the PUT request with Basic Authentication
    response = requests.put(url, headers=headers, data=payload, auth=HTTPBasicAuth(username, password), verify=False)

    # Print the response status code and text
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
except requests.exceptions.RequestException as e:
    # Handle any exceptions that occur
    print(f"An error occurred: {e}")
