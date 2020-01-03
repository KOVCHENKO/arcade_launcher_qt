import json
import requests

from Utility.application_config import remote_host


class PhoneInputService:
    def send_phone(self, phone_number: str):
        phone_data = {
            'phone': phone_number,
            # stub for response
            'response': 'success'
        }

        request = requests.post(remote_host + 'post', data=phone_data)
        json_response = request.text

        return json.loads(json_response)

    def resolve_phone_request(self, phone_number: str):
        response = self.send_phone(phone_number)

        return response.get('json').get('response') == 'success'
