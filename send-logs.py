import requests
import json
from datetime import datetime
import socket
import base64

# Replace the URL with your Parseable URL and stream name
url = "http://0.0.0.0:8000/api/v1/logstream/namesdir"

# Get the current timestamp in the desired format
current_timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")

# Get the local machine's hostname
local_hostname = socket.gethostname()

# JSON payload to send
payload = json.dumps([
    {
        "id": "434a5f5e-2f5f-11ed-a261-asdasdafgdfd",
        "datetime": current_timestamp,
        "host": local_hostname,  # Using the local machine's hostname
        "user-identifier": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "method": "PUT",
        "status": 500,
        "referrer": "http://www.google.com/"
    }
])

# Encode the username and password as Base64
username_password = "admin:admin"
encoded_credentials = base64.b64encode(username_password.encode()).decode()

# Headers
headers = {
    # Custom metadata
    "X-P-META-Host": "192.168.1.3",
    # Tags
    "X-P-TAG-Language": "python",
    # Basic auth credentials
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/json"
}

try:
    # Make the POST request
    response = requests.post(url, headers=headers, data=payload)

    # Raise an HTTPError if the response was an HTTP error
    response.raise_for_status()

    # Print the response
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # HTTP error
except requests.exceptions.ConnectionError as conn_err:
    print(f"Error connecting: {conn_err}")  # Connection error
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")  # Timeout error
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")  # General error
