import urllib.request
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        with urllib.request.urlopen(self.url) as response:
            return response.read()   # <-- RETURN RAW BYTES (NO DECODE)

    def load_json(self):
        body = self.get_response_body()
        decoded = body.decode("utf-8")   # decode only for JSON conversion
        return json.loads(decoded)
# Example usage:
# requester = GetRequester("https://api.example.com/data")
# data = requester.load_json()