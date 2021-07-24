import requests
import json

class ScanHandler:
    def scanner(payload):
        try:
            url = 'https://domain.com/ocr'
            response = requests.post(
                url,
                data=payload
            )
            r = json.load(response.text)
            return r
        except Exception as e:
            print(e)
    
