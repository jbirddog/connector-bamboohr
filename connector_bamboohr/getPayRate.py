import requests

class GetPayRate:
    def __init__(self, api_key: str, subdomain: str, employee_id: str):
        self.api_key = api_key
        self.subdomain = subdomain
        self.employee_id = employee_id

    def execute(self):
        url = f'https://api.bamboohr.com/api/gateway.php/{self.subdomain}/v1/employees/{self.employee_id}'
        headers = { 'Accept': 'application/json' }
        params = { 'fields': 'payRate', 'onlyCurrent': 'true' }
        auth = (self.api_key, 'x')

        # TODO: error handling
        response = requests.get(url, params, headers=headers, auth=auth)

        return {
            'response': response.text,
            'status': 200,
            'mimetype': 'application/json'
        }
