import json
import requests

from Utility.application_config import remote_host


class PhoneInputService:
    def send_phone(self, phone_number: str):
        phone_data = {
            'phone': phone_number
        }

        request = requests.post(remote_host + 'post', data=phone_data)
        json_response = request.text

        response = json.loads(json_response)
        print(response.get('json'))
