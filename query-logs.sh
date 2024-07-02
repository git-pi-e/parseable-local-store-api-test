curl -X POST \
  -H "Authorization: Basic YWRtaW46YWRtaW4=" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "select * from namesdir",
    "startTime": "'"$(date -u +"%Y-%m-%dT%H:%M:%SZ" --date='-1 hour')"'",
    "endTime": "'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'"
  }' \
  http://0.0.0.0:8000/api/v1/query

# Basic auth is base64 encoded admin:admin